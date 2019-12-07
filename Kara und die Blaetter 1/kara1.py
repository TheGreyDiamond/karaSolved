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
  if kara.onLeaf():   ## Kara steht auf einem Blatt, also wird es aufgenommen
    kara.removeLeaf()
  else:               ## Die erste Kondition ist nicht erfüllt, also wird ein Blatt hingelegt
    kara.putLeaf()
  kara.move()

        