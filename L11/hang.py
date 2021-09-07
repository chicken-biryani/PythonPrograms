from tkinter import*
from tkinter import messagebox
import random
from string import ascii_uppercase

main = Tk()
main.title("Hangman")
main.geometry("")
main.configure(bg='grey')

photos = [PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang0.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang1.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang2.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang3.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang4.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang5.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang6.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang7.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang8.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang9.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang10.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Proj\\images\\hang11.png")]

imgLabel=Label(main)
imgLabel.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
imgLabel.config(image=photos[0])



def words():
	
	no=random.randint(1,4)
	if(no==1):
		
		Colors=['Orange','Yellow','Green','Blue','Brown','Magenta','Olive','Maroon','Navy','Turquoise','Silver','Lime','Teal','Indigo','Violet','Pink','Black','White','Grey']
		return random.choice(Colors)
	elif(no==2):
		
		Country=['India','Denmark','Iceland','Switzerland','Netherlands','Canada','New Zealand','Australia','Spain','Russia','Costa Rica','Austria']
		return random.choice(Country)
	elif(no==3):
		
		Animals=['Squirrel','Koala','Elephant','Leopard','Hippopotamus','Giraffe','Dolphin','Reindeer','Peacock','Penguin','Parrot','Flamingo','Woodpecker']
		
		return random.choice(Animals)
	elif(no==4):
		
		Flowers=['Hibiscus','Jasmine','Lily','Lotus','Marigold','Morning glory','Tulip','Rose','Sunflower','Lavender','Cherry blossom']
		return random.choice(Flowers)
	

def newGame():
	global the_word_withSpaces
	global numberofGuesses
	numberofGuesses=0
	imgLabel.config(image=photos[0])
	the_word=words()
	the_word_withSpaces=" ".join(the_word)
	lblWord.set(" ".join("_"*len(the_word)))
	

def guess(letter):
	global numberofGuesses
	if numberofGuesses < 11:
		txt = list(the_word_withSpaces)
		guessed=list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set( " ".join(guessed))
				if lblWord.get() == the_word_withSpaces:
					messagebox.showinfo("Hangman","You guessed it! ")
		else:
			numberofGuesses+=1
			imgLabel.config(image=photos[numberofGuesses])		
			if numberofGuesses==11:
				messagebox.showinfo("Hangman","Game Over ")

#lblword = Label(main, text="_",font=("arial", 18,"bold"))
#lblword.grid()
lblWord=StringVar()
Label(main,textvariable=lblWord,font=("Consolas 24 bold")).grid(row=0,column=3,columnspan=6,padx=10)


n=0
for c in ascii_uppercase:
	Button(main, text=c, command=lambda c=c: guess (c), font=("Helvetica 18"), width=5,bg='skyblue').grid (row=1+n//9, column=n%9)
	n+=1
Button(main,text="New\nGame",command=lambda:newGame(), font=("Helvetica 10 bold"), width=5,bg='light pink').grid(row=3,column=8,sticky="NSWE")
newGame()



main.mainloop()