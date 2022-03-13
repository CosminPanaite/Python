class MyPointValidator:
    def Validate(self, my_point):
        errors = []
        if my_point.colour not in ["red", "green", "blue", "yellow", "magenta"]:
            errors.append("The colour of the point should be in the list ['red','green','blue','yellow','magenta']")
        if len(errors):
            raise ValueError(errors)
