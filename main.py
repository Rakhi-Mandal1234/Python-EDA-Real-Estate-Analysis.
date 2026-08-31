import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('data.csv')


# Data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())
df=df.drop_duplicates()

#Numerical data cleaning
df['price']=df["price"].astype(str).str.replace('$','').str.replace(',','').astype(float)
print(df['price'])
df['area']=df['area'].astype(str).str.replace(',','').astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',','').astype(int)
print(df['rate_per_sqft'])

#Cetagorical data cleaning
df['status']=df['status'].str.strip().str.lower()
df['rera_approval']=(df['rera_approval'].astype(str) .str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False}))
print(df['rera_approval'])
df['flat type']=df['flat_type'].str.strip().str.lower() 
print(df['flat type'])
df=df.drop_duplicates()
print(df.head())
print(df.info())

#Question 1: Which is the costliest flat?
costliest_flat=df.loc[df['price'].idxmax()]
print(f"The costliest flat is a {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000:.2f} crore. It has an area of {costliest_flat['area']} sqft and a rate per sqft of ${costliest_flat['rate_per_sqft']:.2f}. The flat is currently {costliest_flat['status']} and is built by {costliest_flat['builder_name']}. RERA approval status: {'Approved' if costliest_flat['rera_approval'] else 'Not Approved'}.in df.company_name, the flat is listed under {costliest_flat['company_name']} and is part of the {costliest_flat['soceity']} society.")


#Question 2: Which locality has the highest average price?
highest_avg_price_locality=df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

#Question 3 :Which locality has the highest rate per square foot?
highest_avg_rate_locality=df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest average rate per square foot is {highest_avg_rate_locality}.")

#Question 4: Ready-to-move vs Under-construction pricing?
ready_to_move_avg_price=df[df['status']=='ready to move']['price'].mean()
under_construction_avg_price=df[df['status']=='under construction']['price'].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move flats are more expensive on average than under-construction flats.")
else:
    print("Under-construction flats are more expensive on average than ready-to-move flats.")

#Question 5:Do RERA approval affect pricing?
rera_approved_avg_price=df[df['rera_approval']==True]['price'].mean()
rera_not_approved_avg_price=df[df['rera_approval']==False]['price'].mean()
if rera_approved_avg_price> rera_not_approved_avg_price:
    print("RERA approvad properties command a price premium.")
else:
    print("RERA approvad properties do not command a price premium.")

#Question 6 :How does area impact price?
# sns.scatterplot(data=df,x='area',y='price')
#plt.show()

#Question 7:wich BHK configuration is the most expensive on average?
most_expensive_bhk=df.groupby('flat_type')['price'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk}.")

#Question 8: Which property type (Apartment, Floor, Plot) is the costliest?
costliest_property_type=df.groupby('property_type')['price'].mean().idxmax()
print(f"The costliest property type on average is {costliest_property_type}.")

#Question 9:Do certain builders or companies consistently price higher?
print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))
print("The top 5 builders that price higher are :",end="")
top_5_builders=df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder, end=", ")

#Question 10:Are larger homes always more expensive per square foot?
sns.scatterplot(data=df,x='area',y='rate_per_sqft')
plt.title('Area vs Rate per Square Foot')
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Square Foot ($)')
plt.show()






