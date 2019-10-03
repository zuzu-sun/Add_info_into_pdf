# Add_info_into_pdf

**Function fill data into specific position of original pdf.**   
@param position: a dictionary described the positions  2-dim (x, y) of orginal pdf that Each parameter(eg. x)  represent as a list.
          'position_x': [], 'position_y': []   
@param data_to_fill: a list include all data need to be filled into pdf. Must be assigned relevant position.  
@param original_pdf: The pdf to be filled.  
@param destination_pdf: generate new pdf.  
@return: no defined.

## Interface to be use:     

Run this function with specify parameters.      
```
fill_data_in_pdf(position, data_to_fill=data)
```
## For example of parameters:  
    position = {'position_x': [], 'position_y': []}
    data = []    
    position['position_x'].append('315')   
    position['position_y'].append('650')   
    data.append('555')  
    