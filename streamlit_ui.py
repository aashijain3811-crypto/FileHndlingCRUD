# streamlit_crud.py

import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="CRUD File Manager", page_icon="📁", layout="centered")

st.title("📁 CRUD File & Folder Manager")


# -------------------------------
# Helper Function
# -------------------------------
def show_files_and_folders():
    st.subheader("📂 Files & Folders")
    p = Path(".")
    items = list(p.rglob("*"))

    if items:
        for index, item in enumerate(items):
            st.write(f"{index + 1} - {item}")
    else:
        st.info("No files or folders found.")


# Sidebar Menu
menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder",
    ],
)

show_files_and_folders()

# -------------------------------
# CREATE FILE
# -------------------------------
if menu == "Create File":
    st.header("📝 Create File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):
        try:
            p = Path(file_name)

            if p.exists():
                st.warning("File already exists!")
            else:
                with open(file_name, "w") as file:
                    file.write(content)

                st.success("File created successfully!")

        except Exception as e:
            st.error(e)

# -------------------------------
# READ FILE
# -------------------------------
elif menu == "Read File":
    st.header("📖 Read File")

    file_name = st.text_input("Enter file name to read")

    if st.button("Read File"):
        try:
            p = Path(file_name)

            if p.exists():
                with open(file_name, "r") as file:
                    st.text_area("File Content", file.read(), height=300)

            else:
                st.error("File not found!")

        except Exception as e:
            st.error(e)

# -------------------------------
# UPDATE FILE
# -------------------------------
elif menu == "Update File":
    st.header("✏️ Update File")

    file_name = st.text_input("Enter file name")

    update_option = st.radio(
        "Choose Update Type",
        ["Overwrite Content", "Append Content"],
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):
        try:
            p = Path(file_name)

            if p.exists():

                if update_option == "Overwrite Content":
                    with open(file_name, "w") as file:
                        file.write(content)

                elif update_option == "Append Content":
                    with open(file_name, "a") as file:
                        file.write(content)

                st.success("File updated successfully!")

            else:
                st.error("File does not exist!")

        except Exception as e:
            st.error(e)

# -------------------------------
# DELETE FILE
# -------------------------------
elif menu == "Delete File":
    st.header("🗑️ Delete File")

    file_name = st.text_input("Enter file name to delete")

    if st.button("Delete File"):
        try:
            p = Path(file_name)

            if p.exists():
                os.remove(p)
                st.success("File deleted successfully!")

            else:
                st.error("File does not exist!")

        except Exception as e:
            st.error(e)

# -------------------------------
# RENAME FILE
# -------------------------------
elif menu == "Rename File":
    st.header("🔄 Rename File")

    old_name = st.text_input("Enter current file name")
    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):
        try:
            p = Path(old_name)

            if p.exists():
                p.rename(new_name)
                st.success("File renamed successfully!")

            else:
                st.error("File not found!")

        except Exception as e:
            st.error(e)

# -------------------------------
# CREATE FOLDER
# -------------------------------
elif menu == "Create Folder":
    st.header("📁 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):
        try:
            p = Path(folder_name)

            if p.exists():
                st.warning("Folder already exists!")

            else:
                p.mkdir()
                st.success("Folder created successfully!")

        except Exception as e:
            st.error(e)

# -------------------------------
# DELETE FOLDER
# -------------------------------
elif menu == "Delete Folder":
    st.header("❌ Delete Folder")

    folder_name = st.text_input("Enter folder name to delete")

    if st.button("Delete Folder"):
        try: 
            p = Path(folder_name)

            if p.exists():
                p.rmdir()
                st.success("Folder deleted successfully!")

            else:
                st.error("Folder not found!")

        except Exception as e:
            st.error(e)