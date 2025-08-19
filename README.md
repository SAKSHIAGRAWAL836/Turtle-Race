# 🐢 Turtle Race Game – Python Turtle Graphics  

Welcome to the **Turtle Race Game!**  
This project is a fun way to learn Python programming, explore graphical animation, and get hands-on with user interaction.  
The game uses Python’s built-in **turtle** module to simulate a colorful turtle race across the screen.  

---

## 🚀 Features  
- **Interactive Betting:** Place a bet on which turtle (by color) you think will win!  
- **Randomized Race:** Each turtle moves forward by a random amount, making every race unpredictable.  
- **Animated Graphics:** Watch the action unfold visually—no boring console output.  
- **Easy Customization:** Add more turtles, obstacles, or new racing rules with simple code tweaks.  
- **Educational Comments:** The code is documented to help you understand every step.  

---

## 🖥️ Screenshot  
Here’s what the race might look like:  

![Screenshot of Turtle Race - six turtles lined up at the starting line, racing to finish](https://github.com/SAKSHIAGRAWAL836/Turtle-Race/blob/main/images/Screenshot%202025-08-19%20113914.png) 

---

## 🔥 Demo GIF  
See the game in action!  

![Turtle Race GIF](https://github.com/SAKSHIAGRAWAL836/Turtle-Race/blob/main/images/Recording%202025-08-19%20113534.gif)

---

## 📝 How to Play  

1. **Clone the repo:**  
   ```bash
   git clone https://github.com/SAKSHIAGRAWAL836/Turtle-Race/blob/main/main.py
   ```
2. **Run the game:**
   ```bash
    python turtle_race.py
   ```
3. **Place your bet:**
   When prompted, enter the color name of the turtle you predict will win.

4. **Watch the race:**
   Sit back and see if your turtle wins the race! 🎉

---

## 💻 Full Code (with comments)
  ``` python
    
    import turtle
    import random
    
    # --- SCREEN SETUP ---
    is_race_on = False
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput("Guess", 'Who do you think will win the race? Enter a colour:')
    
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []
    
    # --- CREATE THE TURTLES ---
    for i in range(6):
        t = turtle.Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x=-230, y=y_positions[i])
        all_turtles.append(t)
    
    # --- START THE RACE ---
    if user_bet:
        is_race_on = True
    
    while is_race_on:
        for t in all_turtles:
            if t.xcor() > 230:
                is_race_on = False
                winner = t.pencolor()
                print(f"You've {'won' if winner == user_bet else 'lost'}! The {winner} turtle won the race.")
            t.forward(random.randint(0,10))
    
    screen.exitonclick()

  ```
---

## ✨ Customization Ideas

**Add more turtles**: Just update the colors and y_positions lists.
**Change track design:** Draw finish lines or obstacles with turtles.
**Track number of wins per color:** Store results and display a leaderboard.
**Speed power-ups:** Randomly boost turtles for excitement.

---

## 🧑💻 Troubleshooting & Tips

- If the screen freezes, ensure you close the last turtle window before rerunning.
- Use exact color names when betting—case-sensitive!
- For more fun, try replacing turtle shapes or changing background color.

---

## 📚 Learn More

- [Turtle Module Documentation](https://docs.python.org/3/library/turtle.html)
- [Python Random Module](https://docs.python.org/3/library/random.html)

---

## 🤝 Contributing

- Fork the repo and submit a pull request for feature suggestions!

- Reach out by opening an issue if you have questions or bug reports.

---

## 📢 Share Your Results!

- Post a screenshot or GIF of your turtle race.
- Who won most often in your runs? What wild track designs did you invent?

**Tag me or submit via Issues!**

