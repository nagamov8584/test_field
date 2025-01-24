import streamlit as st

def find_account(input_string):
    res = re.search(r'\d{20}', input_string)
    return res[0]
def data_uploader():
    data = st.file_uploader(label="upload txt file")
    return data
def read_file(file):
    with io.open(file, "r") as original_file:
        content = original_file.readlines()
        return content
    
def write_file(container, data):
    for line in data:
        container.write(line)

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


st.title("Test field for txt preparation")

input_data = data_uploader()
text_container = st.container()
input_file = read_file(input_data)
write_file(text_container, input_file)



