# Challenge Three: The Appraisal Engine


"""
PROCEDURE shop_sell(inventoryMoney, gem_inventory) {
    DISPLAY "What have you got to sell?"
    
    IF (LENGTH(gem_inventory) = 0) {
        DISPLAY "If ya ain't got nothing to sell, why ya bothering me?"
        RETURN inventoryMoney
    }
    
    DISPLAY "--- Your Gems ---"
    i ← 1
    FOR EACH gem IN gem_inventory {
        // If the value (index 2) is 0, hide the rarity
        IF (gem[2] = 0) {
            DISPLAY i + ". Unappraised " + gem[1]
        } ELSE {
            DISPLAY i + ". " + gem[3] + " " + gem[1] + " (Value: $" + gem[2] + ")"
        }
        i ← i + 1
    }
    
    DISPLAY "Enter the number of the gem you want to sell:"
    choice ← INPUT()
    
    IF (choice < 1 OR choice > LENGTH(gem_inventory)) {
        DISPLAY "You don't have that gem! Stop wasting my time!"
        RETURN inventoryMoney
    }
    
    selectedGem ← gem_inventory[choice]
    gemName ← selectedGem[1]
    gemValue ← selectedGem[2]
    gemRarity ← selectedGem[3]
    
    IF (gemRarity = "appraised_fake") {
        DISPLAY "Now look here, I ain't in the business of buying fakes."
        RETURN inventoryMoney
    }
    
    IF (gemValue = 0) {
        DISPLAY "Looks like this hasn't been appraised yet. Let me see..."
        
        IF (gemRarity = "common") {
            gemValue ← RANDOM(2, 5)
        } ELSE IF (gemRarity = "uncommon") {
            gemValue ← RANDOM(7, 10)
        } ELSE IF (gemRarity = "rare") {
            gemValue ← RANDOM(12, 20)
        } ELSE IF (gemRarity = "unique") {
            gemValue ← RANDOM(25, 50)
        } ELSE {
            gemValue ← 0
            gemRarity ← "appraised_fake"
        }
        
        selectedGem[2] ← gemValue
        selectedGem[3] ← gemRarity
        gem_inventory[choice] ← selectedGem
    }
    
    IF (gemRarity ≠ "appraised_fake") {
        DISPLAY "Ah yes. I'd be willing to offer you $" + gemValue + " for that."
        DISPLAY "Interested? Y/N"
        accept ← INPUT()
        
        IF (accept = "y" OR accept = "Y") {
            inventoryMoney ← inventoryMoney + gemValue
            REMOVE(gem_inventory, choice)
            DISPLAY "Transaction complete!"
        }
    } ELSE {
        DISPLAY "Now look here, I ain't in the business of buying fakes."
    }
    
    RETURN inventoryMoney
}
"""

import random

def shop_sell(inventory, gem_inventory):
    # Write your translated Python code below this line!
    pass

    print("What have you got to sell?")
    
    if len(gem_inventory) == 0:
        print("If ya ain't got nothing to sell, why ya bothering me?")
        return inventory['money']
    
    print("--- Your Gems ---")
    i = 1
    for gem in gem_inventory:
        if (gem[1] == 0):
            print(i ,". Unappraised " , gem[1])
        else:
            print(i ,". " , gem[2] , " " , gem[0] , " (Value: $" , gem[1] , ")")
        i = i + 1
          
    print("Enter the number of the gem you want to sell:")
    choice = int(input())
    if (choice < 1 or choice > len(gem_inventory)):
        print("You don't have that gem! Stop wasting my time!")
        return inventory['money']
        
    selectedGem = gem_inventory[choice]
    gemName = selectedGem[0]
    gemValue = selectedGem[1]
    gemRarity = selectedGem[2]
    
    if (gemRarity == "appraised_fake"):
        print("Now look here, I ain't in the business of buying fakes.")
        return inventory['money']
        
    if (gemValue == 0):
        print("Looks like this hasn't been appraised yet. Let me see...")
            
        if gemRarity == "common":
            gemValue = random.randint(2, 5)
        elif gemRarity == "uncommon":
            gemValue = random.randint(7, 10)
        elif gemRarity == "rare":
            gemValue = random.randint(12, 20)
        elif (gemRarity == "unique"):
            gemValue = random.randint(25, 50)
        else:
            gemValue = 0
            gemRarity = "appraised_fake"
            
        selectedGem[1] = gemValue
        selectedGem[2] = gemRarity
        gem_inventory[choice] = selectedGem
    if gemRarity != "appraised_fake":
        print("Ah yes. I'd be willing to offer you $" + str(gemValue) + " for that.")
        print("Interested? Y/N")
        accept = input()



    if (gemRarity != "appraised_fake"):
        print("Ah yes. I'd be willing to offer you $" + str(gemValue) + " for that.")
        print("Interested? Y/N")
        accept = input()
        
        if (accept == "y" or accept == "Y"):
            inventory['money'] = inventory['money'] + gemValue
            gem_inventory.pop(choice)
            print("Transaction complete!")
        else: 
            print("Now look here, I ain't in the business of buying fakes.")
    
    
    return inventory['money']