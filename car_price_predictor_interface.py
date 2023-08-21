import pandas as pd
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp = """
    <div style="background-color: lightblue; padding: 16px">
    <h2 style="color: black; text-align: center;">Car Price Prediction Using ML</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.write('')
    st.write('')

    st.markdown("##### Do you want to sell your car? \n ##### Check below our AI car price calculator!")

    p1 = st.number_input("What is the current price of your car (In Lakhs)?",2.5,25.0,step=1.0)

    p2 = st.number_input("How many kilometers were driven in this car?",0,5000000,step=1000)

    s1 = st.selectbox("What is the fuel type of the car", ('Petrol','Diesel','CNG'))

    if s1 == "CNG":
        p3=True
        p4=False
        p5=False
    elif s1 == "Diesel":
        p3=False
        p4=True
        p5=False
    elif s1 == "Petrol":
        p3=False
        p4=False
        p5=True    

    s2 = st.selectbox("Are you a Dealer or Individual?", ('Dealer','Individual'))

    if s2 == "Dealer":
        p6=True
        p7=False
    elif s1 == "Individual":
        p6=False
        p7=True

    s3 = st.selectbox("What is the transmission type?", ('Automatic','Manual'))

    if s2 == "Dealer":
        p8=True
        p9=False        
    elif s1 == "Individual":
        p8=False
        p9=True

    p10 = st.slider("Number of owners the car previously had?",0,3)

    now_time = datetime.datetime.now()

    years = st.number_input("In which year car was purchased?",1990,now_time.year)
    p11 = now_time.year - years

    model = xgb.XGBRegressor()
    model.load_model('xgbr_model.json')

    test_data = pd.DataFrame({
        'Present_Price':p1,
        'Kms_Driven':p2,
        'Owner':p10,
        'Years_old':p11,
        'Fuel_Type_CNG':p3,
        'Fuel_Type_Diesel':p4, 
        'Fuel_Type_Petrol':p5, 
        'Seller_Type_Dealer':p6,
        'Seller_Type_Individual':p7, 
        'Transmission_Automatic':p8,
        'Transmission_Manual':p9
    },index=[0])

    if st.button('Predict'):
        pred = model.predict(test_data)
        try:
            if pred > 0:
                st.balloons()
                st.success("You can sell your car for {:.2f} Lakhs".format(pred[0]))
            else:
                st.warning("You're not able to sell this car")
        except:
            st.warning("Something went wrong, please try again")

if __name__ == '__main__':
    main()
