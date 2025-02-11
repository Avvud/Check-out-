import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Simple Streamlit App")
    st.write("This is a basic Streamlit application.")
    
    # Text Input
    user_input = st.text_input("Enter some text:")
    if user_input:
        st.write("You entered:", user_input)
    
    # Simple Chart
    st.subheader("Random Data Plot")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sine Wave")
    ax.legend()
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()
