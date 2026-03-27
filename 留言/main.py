import streamlit as st

st.title('留言栏')
recv = st.chat_input('输入你要的内容')

with open('留言.txt', 'r') as file:
    data = file.read()
    bata = data.split('//')
    lst = bata  
    lst = [x for x in lst if x != 'None'] 
    with open('留言.txt', 'w') as file:
        for element in lst:
            ele = element + '//'
            file.write(ele)
    print(bata)
    print(lst)

st.divider()

with open('留言.txt', 'r') as file:
    for ale in lst:
            st.write(ale)
    
if recv:
    st.markdown(recv)
    
with open("留言.txt", "a") as file:
    reca = str(recv) + '//'
    file.write(str(recv))

