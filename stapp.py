import json
import time
import requests
import streamlit as st

st.set_page_config(page_title='Simple App', page_icon='<UNK>', layout='centered')
st.image("images/chopy_soup_logo.jpeg", use_container_width=True)
st.header(""":blue[Chopy-Soup] Search App.""", divider="rainbow")

st.html("""<p>Your one-stop shop for a supercharged, tech-tastic shopping experience! We've got all the gadgets, 
glam, and gizmos you could ever dream of, served up with a smile and a sprinkle of future-forward fun!</p>
""")

st.markdown("""Search on our new search engine!""")
user_query = st.text_input(label="Be semantic", placeholder='Search Term')

header: dict[str, str] = {
    "Content-Type": "application/json",
}

semantic_url: str = "http://localhost:8000/semantic-response"

if user_query:
    data: dict[str, str] = {
        "query": user_query,
    }
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(2)
        response = requests.post(url=semantic_url, headers=header, data=json.dumps(data))
        search: list[str] = response.json()["semantic_response"]["response"]

        st.html(f"""<p>Based on your search We've found the best for you!</p>
        <ol>
            <li>{search[0]}</li>
            <li>{search[1]}</li>
            <li>{search[2]}</li>
        </ol>
        """)
        st.success("Awesome!")
