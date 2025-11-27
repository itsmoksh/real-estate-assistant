import streamlit as st
from rag import process_urls,generate
st.title("Real Estate Assistant")

st.sidebar.subheader("Enter Url's")
url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

process_urls_button = st.sidebar.button("Process Urls")
placeholder = st.empty()
if process_urls_button:
    urls = [url for url in [url1,url2,url3] if url!=""]

    if len(urls) == 0:
        placeholder.text("You must provide at least one url")

    else:
        with st.status("Generating results..",expanded=True) as status:
            for url_status in process_urls(urls):
                st.write(url_status)
            status.update(label = "Chunks stored, now you can ask questions",expanded = False)

query = placeholder.text_input("Question")
if query:
    try:
        solution, sources = generate(query)
        st.header("Answer")
        st.write(solution)
        if sources:
            st.header("Source")
            unique_source = set(sources)
            for source in unique_source:
                st.write(source)

    except RuntimeError as e:
        placeholder.text("You must process the Url's first")


