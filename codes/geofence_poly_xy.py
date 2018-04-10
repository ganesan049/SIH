## GeoFencing 
## This script returns true if given
##  (x,y) is inside polygon coordinates of polygon 
##   coordinates.
##   use is_pt_in_poly_4(x,y) - for better result
##
##
class is_xy_inside_poly(object):
    def __init__(self,polyX,polyY,polyCorners):
        self.polyX=polyX
        self.polyY=polyY
        self.polyCorners=polyCorners
        self.const=[0,0,0,0]
        self.muls=[0,0,0,0]
    def initialize_vals(self):
        j=self.polyCorners-1
        for i in range(j+1):
            if self.polyY[j] is self.polyY[i]:
                self.const[i]=self.polyX[i]
                self.muls[i]=0
            else:
                self.const[i]=self.polyX[i]-(self.polyY[i]*self.polyX[j])/(self.polyY[j]-self.polyY[i])+(self.polyY[i]*self.polyX[i])/(self.polyY[j]-self.polyY[i])
                self.muls[i]=(self.polyX[j]-self.polyX[i])/(self.polyY[j]-self.polyY[i])
                j=i;
                
    def is_pt_in_poly(self,x,y):
        j=self.polyCorners-1
        oddNodes=False
        for i in range(j+1):
            if ((self.polyY[i] < y and self.polyY[j] >= y) or (self.polyY[j] < y and self.polyY[i]>=y)):
                oddNodes=(y*self.muls[i] + self.const[i] < x)
            j=i;
        return oddNodes            
    def is_pt_in_poly_2(self,x,y):
        j=self.polyCorners-1
        oddNodes=False
        for i in range(j+1):
            if (self.polyX[i]+(y-self.polyY[i])/(self.polyY[j]-self.polyY[i])*(self.polyX[j]-self.polyX[i])<x):
                oddNodes=not oddNodes
            j=i;
        return oddNodes        
    def is_pt_in_poly_3(self,x,y):
        j=self.polyCorners-1
        oddNodes=False
        for i in range(j+1):
            if (self.polyY[i]<y and self.polyY[j]>=y
    or  self.polyY[j]<y and self.polyY[i]>=y):
                if (self.polyX[i]+(y-self.polyY[i])/(self.polyY[j]-self.polyY[i])*(self.polyX[j]-self.polyX[i])<x):
                    oddNodes=not oddNodes
            j=i;
        return oddNodes
    def is_pt_in_poly_4(self,x,y):
        oddNodes=False
        j=self.polyCorners-1
        for i in range(j+1):
            if ( ((self.polyY[i]>y) != (self.polyY[j]>y)) and
	 (x < (self.polyX[j]-self.polyX[i]) * (y-self.polyY[i]) / (self.polyY[j]-self.polyY[i]) + self.polyX[i]) ):
                oddNodes=not oddNodes
        return oddNodes        








    
                    
