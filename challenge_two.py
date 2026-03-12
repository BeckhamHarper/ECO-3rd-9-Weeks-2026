# Challenge Two: The Shop Menu


"""
PROCEDURE shop_buy(inventoryMoney, inventoryPick, stockList) {
    keepShopping ← "y"
    
    REPEAT UNTIL (keepShopping ≠ "y" AND keepShopping ≠ "Y") {
        DISPLAY "--- Items for Sale ---"
        i ← 1
        FOR EACH item IN stockList {
            DISPLAY i + ". " + item[1] + " - $" + item[2]
            i ← i + 1
        }
        
        DISPLAY "Enter the number of the item you want to buy:"
        choice ← INPUT()
        
        IF (choice ≥ 1 AND choice ≤ LENGTH(stockList)) {
            selectedItem ← stockList[choice]
            itemName ← selectedItem[1]
            itemPrice ← selectedItem[2]
            
            IF (inventoryMoney ≥ itemPrice) {
                inventoryMoney ← inventoryMoney - itemPrice
                
                // Extract 3 characters starting at the 10th letter (1-based)
                IF (SUBSTRING(itemName, 10, 3) = "Enh") {
                    inventoryPick ← "good"
                }
                ELSE IF (SUBSTRING(itemName, 10, 3) = "Gre") {
                    inventoryPick ← "better"
                }
                ELSE IF (SUBSTRING(itemName, 10, 3) = "Sup") {
                    inventoryPick ← "best"
                }
                
                REMOVE(stockList, choice)
                DISPLAY "You bought the " + itemName + "!"
            }
            ELSE {
                DISPLAY "You can't afford that!"
            }
        }
        ELSE {
            DISPLAY "Sorry, we don't have that."
        }
        
        DISPLAY "Keep shopping? Y/N"
        keepShopping ← INPUT()
    }
    
    RETURN inventoryMoney
}
"""

def shop_buy(stock, inventory):
    # Write your translated Python code below this line!
    pass
    keepShopping = "y"
    while keepShopping != "y" or keepShopping != "Y":
        print("--- Items for sale ---")
        i = 1
        for item in range(stock):
            print(i +"." + item[1] + "- $" + item[2])
            i = i+1
        print("Enter the number of the item you want to buy:")
        choice = input()
        if choice >= 1 and choice <= len(stock):
            selectedItem = stockList[choice]
            itemName = selectedItem[1]
            itemPrice = selectedItem[2]
            
            if inventoryMoney >= itemPrice:
                inventoryMoney = inventoryMoney - itemPrice
                if substring(itemName, 10, 3 ) == "Enh":
                    inventory['pick'] = "good"
                elif substring(itemName, 10, 3) == "Gre":
                    inventory['pick'] = "better"
                elif substring(itemName, 10, 3) == "Sup":
                    inventory['pick'] = "best"
                stock.pop(choice)
                print("you bought the " + itemName +"!")
        else:
            print("You can't afford that!")
        print("Keep shopping? Y/N")
        keepShopping = input()
    return inventory['Money']