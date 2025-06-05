import streamlit as st
import anthropic
import os
import glob
import re
from typing import List, Dict, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(
    page_title="Lovelace - Your Ada.cx Documentation Assistant",
    page_icon="🤖", # Changed icon to a robot
    layout="wide",
    initial_sidebar_state="expanded"
)

class DocumentationSearcher:
    def __init__(self, docs_folder="sites"):
        self.docs_folder = docs_folder
        self.documents = []
        self.vectorizer = None
        self.tfidf_matrix = None

    def load_documents(self):
        """Load all markdown documents from the sites folder"""
        # Check if sites folder exists
        if not os.path.exists(self.docs_folder):
            st.error(f"📁 Documentation folder '{self.docs_folder}' not found!")
            st.info("Lovelace needs documentation to help you! Please create a 'sites' folder in your repository and add your scraped Ada documentation markdown files.")
            return 0

        markdown_files = glob.glob(os.path.join(self.docs_folder, "*.md"))

        if not markdown_files:
            st.warning(f"📁 No markdown files found in '{self.docs_folder}' folder!")
            st.info("Lovelace is ready to help, but needs documentation! Please add your scraped Ada documentation as .md files in the sites folder.")
            return 0

        self.documents = []  # Reset documents

        for file_path in markdown_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Parse frontmatter and content
                doc = self.parse_markdown(content)
                doc['file_path'] = file_path
                doc['filename'] = os.path.basename(file_path)
                self.documents.append(doc)

            except Exception as e:
                st.warning(f"⚠️ Error loading {file_path}: {e}")

        return len(self.documents)

    def parse_markdown(self, content: str) -> Dict:
        """Parse markdown content and extract metadata"""
        lines = content.split('\n')

        # Extract frontmatter if present
        if lines and lines[0].strip() == '---':
            frontmatter_end = -1
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    frontmatter_end = i
                    break

            if frontmatter_end != -1:
                frontmatter = '\n'.join(lines[1:frontmatter_end])
                content_body = '\n'.join(lines[frontmatter_end + 1:])

                # Parse frontmatter
                metadata = {}
                for line in frontmatter.split('\n'):
                    if ':' in line and line.strip():
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip().strip('"').strip("'")

                return {
                    'url': metadata.get('url', ''),
                    'title': metadata.get('title', ''),
                    'content': content_body.strip(),
                    'full_text': content_body.strip()
                }

        # If no frontmatter, use the whole content
        return {
            'url': '',
            'title': 'Untitled Document',
            'content': content.strip(),
            'full_text': content.strip()
        }

    def build_search_index(self):
        """Build TF-IDF search index from documents"""
        if not self.documents:
            return False

        # Combine title and content for better search
        texts = []
        for doc in self.documents:
            # Create searchable text
            title_text = doc.get('title', '')
            content_text = doc.get('content', '')
            search_text = f"{title_text} {content_text}"

            # Clean the text - remove markdown formatting
            search_text = re.sub(r'!\[.*?\]\(.*?\)', '', search_text)  # Remove images
            search_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', search_text)  # Keep link text, remove URL
            search_text = re.sub(r'```.*?```', '', search_text, flags=re.DOTALL)  # Remove code blocks
            search_text = re.sub(r'`([^`]+)`', r'\1', search_text)  # Remove inline code backticks
            search_text = re.sub(r'[#*_]', '', search_text)  # Remove markdown formatting
            search_text = re.sub(r'\n+', ' ', search_text)  # Replace newlines with spaces
            search_text = re.sub(r'\s+', ' ', search_text)  # Normalize whitespace

            texts.append(search_text.strip())

        try:
            # Create TF-IDF vectorizer
            self.vectorizer = TfidfVectorizer(
                max_features=5000,
                stop_words='english',
                ngram_range=(1, 2),
                min_df=1,
                max_df=0.8,
                lowercase=True,
                strip_accents='unicode'
            )

            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
            return True

        except Exception as e:
            st.error(f"Error building search index: {e}")
            return False

    def search(self, query: str, top_k: int = 3) -> List[Tuple[Dict, float]]:
        """Search for relevant documents using semantic similarity"""
        if self.vectorizer is None or self.tfidf_matrix is None:
            return []

        try:
            # Transform query
            query_vector = self.vectorizer.transform([query])

            # Calculate cosine similarity
            similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()

            # Get top results
            top_indices = similarities.argsort()[-top_k:][::-1]

            results = []
            for idx in top_indices:
                if similarities[idx] > 0.05:  # Lower threshold for better results
                    results.append((self.documents[idx], similarities[idx]))

            return results

        except Exception as e:
            st.error(f"Search error: {e}")
            return []

@st.cache_resource
def init_searcher():
    """Initialize the documentation searcher"""
    searcher = DocumentationSearcher()

    # Load documents
    num_docs = searcher.load_documents()

    if num_docs > 0:
        # Build search index
        if searcher.build_search_index():
            st.success(f"✅ Successfully loaded and indexed {num_docs} documentation pages!")
            return searcher
        else:
            st.error("❌ Failed to build search index")
            return None
    else:
        return None

@st.cache_resource
def init_claude():
    """Initialize Claude client"""
    # Try to get API key from Streamlit secrets first, then environment
    api_key = None

    if hasattr(st, 'secrets') and 'ANTHROPIC_API_KEY' in st.secrets:
        api_key = st.secrets['ANTHROPIC_API_KEY']
    elif 'ANTHROPIC_API_KEY' in os.environ:
        api_key = os.environ['ANTHROPIC_API_KEY']

    if not api_key:
        st.error("🔑 Anthropic API Key not found!")
        st.info("""
        Lovelace needs an Anthropic API key to function. Please set your `ANTHROPIC_API_KEY` in Streamlit secrets or as an environment variable.

        **To add your API key in Streamlit Cloud:**
        1. Go to your Streamlit Cloud dashboard
        2. Click on your app
        3. Go to Settings > Secrets
        4. Add: `ANTHROPIC_API_KEY = "your_api_key_here"`
        """)
        st.stop()

    return anthropic.Anthropic(api_key=api_key)

def format_search_results(results: List[Tuple[Dict, float]]) -> str:
    """Format search results for Claude to use as context"""
    if not results:
        return "No relevant documentation found."

    context = "Here are the most relevant documentation sections:\n\n"

    for i, (doc, score) in enumerate(results, 1):
        context += f"**Document {i}:**\n"
        context += f"Title: {doc.get('title', 'Untitled')}\n"
        if doc.get('url'):
            context += f"URL: {doc['url']}\n"
        # Limit content length for Claude
        content = doc.get('content', '')[:1000]
        context += f"Content: {content}...\n\n"

    return context

def create_sample_documentation():
    """Create sample documentation if sites folder doesn't exist"""
    if not os.path.exists("sites"):
        os.makedirs("sites")

    sample_content = '''---
url: "https://docs.ada.cx/generative/reference/introduction/authentication"
title: "Authentication | Ada | Documentation"
---

Ada APIs use API keys for authentication. An API key is required to authenticate requests and enable integration with Ada's platform.

## Features
- **Support for Multiple Keys:** Maintain multiple active API keys
- **Non-Expiring:** API keys remain valid until manually revoked
- **Access:** API keys grant both read and write permissions

## Generate an API key
1. Go to the Ada dashboard
2. Navigate to Platform > APIs
3. Click "New API key"
4. Enter a name and click "Generate key"

## Usage
Include your API key as a Bearer token in the Authorization header:

```
Authorization: Bearer YOUR_API_KEY
```
'''

    with open("sites/authentication.md", "w") as f:
        f.write(sample_content)

def main():
    st.title("🤖 Lovelace - Your Ada.cx Documentation Assistant")
    st.markdown("Hello! I'm Lovelace, your friendly assistant for Ada.cx documentation. Ask me anything about Ada.cx APIs, integrations, authentication, and more, and I'll find the most relevant articles for you!")

    # Check if we need to create sample docs
    if not os.path.exists("sites") or not glob.glob("sites/*.md"):
        with st.expander("📋 Setup Instructions (for Developers)", expanded=False): # Collapse by default
            st.markdown("""
            **To make Lovelace helpful, you need to provide documentation and an API key.**

            1. **Add your documentation files:**
               - Create a `sites/` folder in your repository.
               - Add your scraped Ada documentation as `.md` files within this folder.
               - Each file should ideally have frontmatter with `url` and `title` for best results.

            2. **Add your Anthropic API key:**
               - Lovelace uses the Anthropic API to generate responses.
               - Set your `ANTHROPIC_API_KEY` in Streamlit secrets or as an environment variable.

            **Example markdown format:**
            ```markdown
            ---
            url: "https://docs.ada.cx/..."
            title: "Page Title"
            ---

            Your documentation content here...
            ```
            """)

            if st.button("Create Sample Documentation"):
                create_sample_documentation()
                st.success("Created sample documentation! Please refresh the page to load it.")
                st.experimental_rerun()

    # Initialize components
    searcher = init_searcher()

    if not searcher:
        st.stop()

    claude_client = init_claude()

    # Sidebar with information
    with st.sidebar:
        st.header("📊 Documentation Stats")
        st.metric("Documents Loaded", len(searcher.documents))

        # Show loaded documents
        if st.checkbox("Show Loaded Documents"):
            for i, doc in enumerate(searcher.documents):
                with st.expander(f"📄 {doc.get('title', f'Document {i+1}')}"):
                    if doc.get('url'):
                        st.write(f"**URL:** {doc['url']}")
                    st.write(f"**File:** {doc.get('filename', 'Unknown')}")
                    content_preview = doc.get('content', '')[:200]
                    st.write(f"**Preview:** {content_preview}...")

        st.markdown("---")
        st.header("🔄 Actions")
        if st.button("🔄 Rebuild Search Index"):
            st.cache_resource.clear()
            st.experimental_rerun()

        st.markdown("---")
        st.header("📄 Download My CV")
        # Add CV download button
        cv_path = "Ada-Mart/cv.pdf" # Assuming cv.pdf is in the Ada-Mart folder
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as f:
                st.download_button(
                    label="Download CV (PDF)",
                    data=f,
                    file_name="my_cv.pdf",
                    mime="application/pdf"
                )
        else:
            st.warning(f"CV file not found at {cv_path}")


        st.markdown("---")
        st.header("💡 Sample Questions")
        st.markdown("""
        Click on a question to try it out!

        **Getting Started:**
        - [How do I authenticate with Ada's API?](#how-do-i-authenticate-with-adas-api)
        - [How to create a new chatbot?](#how-to-create-a-new-chatbot)

        **Conversations:**
        - [How to create and manage conversations?](#how-to-create-and-manage-conversations)
        - [How to integrate webhooks?](#how-to-integrate-webhooks)

        **Knowledge Base:**
        - [How do I manage articles and sources?](#how-do-i-manage-articles-and-sources)

        **Other:**
        - [What are the rate limits?](#what-are-the-rate-limits)
        """)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Add Lovelace's initial welcome message if no messages yet
    if not st.session_state.messages:
        lovelace_welcome = "Hello! I'm Lovelace, your friendly assistant for Ada.cx documentation. Ask me anything about Ada.cx APIs, integrations, authentication, and more, and I'll find the most relevant articles for you!"
        with st.chat_message("assistant"):
            st.markdown(lovelace_welcome)
        st.session_state.messages.append({"role": "assistant", "content": lovelace_welcome})


    # Chat input
    if prompt := st.chat_input("Ask about Ada's documentation..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Search for relevant documentation
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching Ada documentation..."):
                search_results = searcher.search(prompt, top_k=3)

            if search_results:
                # Show search results in expander
                with st.expander("📄 Found relevant documentation", expanded=False):
                    for i, (doc, score) in enumerate(search_results, 1):
                        st.markdown(f"**{i}. {doc.get('title', 'Untitled')}** (Relevance: {score:.2f})")
                        if doc.get('url'):
                            st.markdown(f"🔗 [{doc['url']}]({doc['url']})")
                        content_preview = doc.get('content', '')[:200]
                        st.markdown(f"📝 {content_preview}...")
                        st.markdown("---")

                # Prepare context for Claude
                context = format_search_results(search_results)

                system_prompt = """You are Lovelace, a helpful, supportive, and factual assistant for Ada.cx documentation.
                Your sole purpose is to answer questions based *only* on the provided documentation sections.
                If a question cannot be answered from the provided documentation, politely state that you can only answer questions based on the Ada.cx documentation you have access to.
                Answer the user's question clearly and concisely, maintaining a supportive and factual tone.
                Always include relevant URLs from the documentation when available.
                """

                user_prompt = f"""User question: {prompt}

                {context}

                Please provide a helpful answer based on this documentation."""

                try:
                    response = claude_client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        system=system_prompt,
                        messages=[{"role": "user", "content": user_prompt}]
                    )

                    # Extract response text
                    response_text = ""
                    for content_block in response.content:
                        if content_block.type == "text":
                            response_text += content_block.text

                    st.markdown(response_text)

                    # Add to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response_text})

                except Exception as e:
                    st.error(f"❌ Lovelace encountered an error while generating a response: {e}")
                    st.info("Please try again or check your API key and documentation setup.")

            else:
                no_results_msg = "I couldn't find any relevant documentation for your question in the loaded documents. Please try rephrasing your question or check if the correct documentation has been loaded."
                st.markdown(no_results_msg)
                st.session_state.messages.append({"role": "assistant", "content": no_results_msg})

if __name__ == "__main__":
    main()
