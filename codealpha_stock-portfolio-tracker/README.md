# Stock Portfolio Tracker

A robust, object-oriented command-line Python application designed to manage, track, and analyze your stock investments efficiently.

## ✨ Features Implemented

### 📈 Portfolio Management
- **Add Stocks**: Seamlessly add stock symbols and quantities to your holdings.
- **Remove Stocks**: Delete specific stock entries from your current portfolio.
- **Search Stock**: Instantly look up detailed stats (quantity, price, value) for any stock you own.
- **Clear Portfolio**: Wipe your entire portfolio with a single command (includes a safety confirmation prompt).
- **Auto-Save**: Changes are automatically and silently saved to `portfolio.csv` after every action (Add/Remove/Clear).

### 📊 Advanced Analytics & UI
- **Detailed Portfolio View**: Displays a professionally formatted table with:
  - Stock Symbol & Quantity
  - Current Price & Total Value
  - **Portfolio Weight**: Automatic percentage distribution for each holding.
- **Diversification Analysis**: Built-in intelligence that warns you if your portfolio isn't diversified enough (fewer than 3 stocks).
- **Investment Summary**: Highlights Total Portfolio Value and your **Top Holding** by value.
- **Visual Allocation Chart**: ASCII-based bar chart using solid blocks (`█`) to visualize your investment distribution.
- **Clean UI**: Integrated clear screen functionality and emoji feedback for an enhanced user experience.

### 💾 Architecture & Data Handling
- **Object-Oriented Design (OOP)**: Built with a scalable `StockTracker` class for better maintainability.
- **CSV Persistence**: Automatic loading and saving from `portfolio.csv` ensures your data is never lost.
- **Input Validation**: Robust error handling for stock symbols and positive integer quantity checks.

## 🛠️ Technologies Used
- **Python 3**: Core logic and object-oriented architecture.
- **CSV Module**: For data persistence and history management.
- **OS Module**: For terminal control and clear screen functionality.

## 🚀 How to Run

1. **Clone or download** the project to your local machine.
2. **Navigate** to the project folder in your terminal.
3. **Run the program**:
   ```bash
   python main.py
   ```

## 📋 Menu Options
1. **Add Stock**: Enter symbol and quantity (Auto-saves).
2. **View Portfolio**: See detailed stats, weights, and diversification analysis.
3. **Search Stock**: Find details of a specific holding.
4. **Show Allocation Chart**: Visual bar chart of your portfolio.
5. **Remove Stock**: Delete a specific stock (Auto-saves).
6. **Clear Portfolio**: Delete all data with confirmation.
7. **Clear Screen**: Refresh and tidy the terminal view.
8. **Exit**: Safely close the application.

## 👤 Author
**Sheethal DP**  
*CodeAlpha Internship Project*
