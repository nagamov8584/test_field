import streamlit as st
import io, re
from io import StringIO
import zipfile

def find_account(input_string):
    res = re.search(r'\d{20}', input_string)
    return res[0]
def data_uploader():
    data = st.file_uploader(label="upload txt file")
    return data
def read_file(file):
    # get UploadedFile data type
    content_bytes = file.getvalue() # we get bytes
    content_string = StringIO(content_bytes.decode("cp1251"))
    return content_string   
def create_zip(files):
        zip_buffer = io.BytesIO()
        # Create a Zip file in memory
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:

            for file in files:   
                st.write(file.name)
                zip_file.writestr(file, file.getvalue())
        zip_buffer.seek(0)  # Rewind the buffer to the beginning
        return zip_buffer
def write_files(container, data):
    #for line in data:
    #    container.write(line)
        #container.write(line.decode('cp1251'))



    containers = []
    container = []
    #
    for line in data:
        if "Получатель=" in line:
            container.append(line)
            containers.append(container)
            container = []
        elif "СекцияРасчСчет" in line:
            containers.append(container)
            container = []
            container.append(line)
        else:
            container.append(line)
    containers.append(container)
    #
    header = containers[0]
    date = containers[1][:2]
    accounts = [[x] for x in containers[1][2:]]
    statements = containers[2:]
    ending = ['КонецФайла']
    #
    txt_files = []
    #
    for iter_account, iter_statement in zip(accounts, statements):
        iter_file = ''

    iter_file = header + date  + iter_account + iter_statement + ending
    txt_files.append(iter_file)

    return accounts, txt_files
    
def work():

    with io.open("source_file.txt", "r", encoding='ascii') as original_file:
        content = original_file.readlines()

        containers = []
        container = []

        for line in content:
            if "Получатель=" in line:
                container.append(line)
                containers.append(container)
                container = []
            elif "СекцияРасчСчет" in line:
                containers.append(container)
                container = []
                container.append(line)
            else:
                container.append(line)
        containers.append(container)

    return x
def download_zip(files, db):
    if st.button('Download txt files'):
        if files:
            zip_buffer = create_zip(files)
            st.download_button(
                label="Download ZIP of txt's",
                data=zip_buffer,
                file_name="txt_files.zip",
                mime="application/zip",
                icon=":material/barcode:"
            )
        else:
            st.warning("Please upload some PDF files first.")

st.title("Test field for txt preparation")

input_data = data_uploader() # UploadedFile type
text_container = st.container()

if input_data:

    input_file = read_file(input_data)
    txt_accounts, files = write_files(text_container, input_file)
    
    


