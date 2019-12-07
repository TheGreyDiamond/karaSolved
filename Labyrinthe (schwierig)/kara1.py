# BEFEHLE:  kara.
#   move()  turnRight()  turnLeft()
#   putLeaf()  removeLeaf()
#
# SENSOREN: kara.
#   treeFront()  treeLeft()  treeRight()
#   mushroomFront()  onLeaf()
#

# hier können Sie eigene Methoden definieren

# hier kommt das Hauptprogramm hin, zB:
while True:
  if kara.treeLeft() == False:
    kara.turnLeft()
    kara.move()
  else:
    if kara.treeFront() == True and kara.treeRight() == False:
        kara.turnRight()
    elif kara.treeFront() == True and kara.treeLeft() == False:
        kara.turnLeft()
    elif kara.treeFront() == True and kara.treeRight() == True and kara.treeLeft() == True:
        kara.turnLeft()
        kara.turnLeft()
    else:
        kara.move()
    if kara.onLeaf() == True:
        kara.removeLeaf()
        break
        exit