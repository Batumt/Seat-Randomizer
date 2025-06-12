import streamlit as st
import random
import math

st.title("Student Seat Randomizer")

names_input = st.text_area("Enter student names (one per line):")

class_name = st.text_input("Class name (e.g., 10-A):")

if st.button("Randomize"):
    names_list = [name.strip() for name in names_input.split("\n") if name.strip()]
    
    if not names_list:
        st.error("Please enter at least one student name.")
    else:
        random.shuffle(names_list)
        
        desk = math.ceil(len(names_list) / 2)
        
        seat_list = []
        for i in range(0, len(names_list), 2):
            pair = names_list[i:i+2]
            seat_list.append(pair)
        
        st.subheader("Seating arrangement:")
        for idx, pair in enumerate(seat_list, start=1):
            st.write(f"desk {idx}: {', '.join(pair)}")
        
        filename = f"{class_name if class_name else 'class'}_seating.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            for idx, pair in enumerate(seat_list, start=1):
                f.write(f"desk {idx}: {', '.join(pair)}\n")
        
        st.success(f"Seating arrangement saved to '{filename}'.")
        
        with open(filename, "r", encoding="utf-8") as f:
            file_data = f.read()
        
        st.download_button("Download seating file", data=file_data, file_name=filename)
