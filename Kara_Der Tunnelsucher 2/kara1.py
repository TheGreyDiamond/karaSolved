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
tunnel = False
while not kara.treeFront():
  if kara.treeRight and kara.treeLeft:
    tunnel = True
  if tunnel:
    if kara.treeRight == False or kara.treeLeft == False:
        break
  kara.move()

        