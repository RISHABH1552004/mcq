from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Rishabh",
    author_email="mohitkumar552004@gmail.com",
    install_reuires = ["openai","langchain","langchain_community","streamlit","pyPDF2","python-dotenv"],
    packages=find_packages()

)