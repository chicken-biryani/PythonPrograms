import matplotlib.pyplot as plt

subject =['mech','bee','math']
marks=[78,99,82]

plt.barh(subject,marks) #barh gives horizontal direction mein bar

plt.title("Mr.amit's score")
plt.ylabel("subject")
plt.xlabel("marks")
plt.show()