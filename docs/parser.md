# Diagram Parser

## Preconditions of the Input Diagram

The diagram parser only works (correctly) on input with the following assumptions. 

* The diagram needs to be exported by Draw.io as an xml output file. 

* The arrows need to be linked between two control structures. You can draw the arrows to point to where the objects are, but the parser requires them to be properlly linked. 

* All text needs to be a part of the diagrams. 

* Action arrows need to either be start with the key term 'Action' or originate from a rectangle completely above another. 
If the two rectangles overlap horizontally, they controller process will be the rectangle that starts at the left most position. 

* Similarly, Feedback arrows need to either be start with the key term 'Feedback' or originate from a rectangle completely below another. 
If the two rectangles overlap horizontally, they controller process will be the rectangle that starts at the left most position. 