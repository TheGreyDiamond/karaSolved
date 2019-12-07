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
while not kara.treeFront():
  if kara.treeLeft() and kara.treeRight(): ## Wenn Links und Rechts ein Baum neben Kara ist
    break ## Dann breche mit break aus dem Loop aus
  else:  ## Sonst
    kara.move() ## Gehe einfach weiter

        