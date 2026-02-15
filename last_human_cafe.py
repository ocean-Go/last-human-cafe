#!/usr/bin/env python3
"""
🎮 The Last Human Cafe - A Text Adventure
Written by Codex + Jarvis
"""

import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_header():
    print("""
    ☕🌍 THE LAST HUMAN CAFE 🌍☕
    =============================
    You are Zog, an alien who just opened 
    Earth's first coffee shop for the last humans!
    ============================================""")

def encounter_customer(rating):
    customers = [
        ("👽 Steve", "I want my coffee... as dark as the void of space. Also, do you have any galactic croissants?"),
        ("🧙‍♀️ Grandma Gladys", "Dear, I've been drinking coffee since before your species existed. Make it STRONG."),
        ("🤖 Robot 3000", "BEEP BOOP. I require 97.3% caffeine. Also, is this wifi password 'password123'?")
    ]
    
    name, order = random.choice(customers)
    slow_print(f"\n🚪 Customer enters: {name}")
    slow_print(f"🗣️ '{order}'")
    
    print("\nYour response options:")
    print("  [1] 🤗 Friendly - 'Welcome! Let me prepare something special!'")
    print("  [2] 😎 Cool - 'Yeah, I got you. One cosmic brew coming up.'")
    print("  [3] 🧠 Smart - 'Ah, a sophisticated choice! I'll add some stardust.'")
    
    choice = input("\n👉 Choice [1-3]: ").strip() or "1"
    
    if choice == '1':
        slow_print("\n✨ You beam warmly. The customer smiles!")
        return random.randint(15, 25)
    elif choice == '2':
        slow_print("\n😎 You nod coolly. The customer seems impressed.")
        return random.randint(10, 20)
    else:
        slow_print("\n🧠 You explain the science behind your brew. The customer is fascinated!")
        return random.randint(20, 30)

def game():
    rating = 50
    print_header()
    
    slow_print("\n🌍 Welcome to Earth, Zog! The humans need their coffee...")
    slow_print("💡 Your mission: Run a successful cafe and earn the trust of humans!")
    
    for day in range(1, 4):
        print(f"\n\n📅 DAY {day}")
        print("=" * 40)
        
        rating += encounter_customer(rating)
        rating = min(100, max(0, rating))
        
        print(f"\n📊 Current Rating: {rating}/100")
        time.sleep(1)
    
    # Ending
    print("\n" + "=" * 40)
    print("🌟 FINAL RATING RESULTS 🌟")
    print("=" * 40)
    
    if rating >= 80:
        print("""
        🏆 TROPHEYS - BEST CAFE IN THE GALAXY!
        
        The humans absolutely LOVE your cafe!
        You've become a local celebrity.
        Even aliens from nearby planets come to visit.
        
        🎉 YOU WIN! Humanity is saved by coffee! 🎉
        """)
    elif rating >= 50:
        print("""
        ⭐ DECENT - NOT BAD, ZOG!
        
        Your cafe is doing okay.
        Some humans come regularly.
        There's room for improvement...
        
        🤔 Maybe try being friendlier? 🤔
        """)
    else:
        print("""
        💀 CLOSED - OH NO!
        
        The humans didn't like your coffee...
        Or maybe it was that incident with the translator...
        
        👽 Better luck on the next planet, Zog!
        """)
    
    print(f"\nFinal Rating: {rating}/100")

if __name__ == "__main__":
    game()
