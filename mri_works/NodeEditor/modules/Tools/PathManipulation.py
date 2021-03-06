class addToList_dyn():
    def __init__(self,list_path=['path'],element_path='path',**dynamicsInputs):
        self.newList=[]
        self.newList.extend(list_path)
        self.newList.append(element_path)
        for di in dynamicsInputs:
            self.newList.append(dynamicsInputs[di])
            
    def newList_path(self:'list_path'):
        return self.newList
        
###############################################################################

class separatePath():

    def __init__(self, inPath="path"):
        import os
        self.inPath = inPath
        self.dir = os.path.dirname(self.inPath)
        tmp = os.path.basename(self.inPath)
        self.name = ('.').join(tmp.split('.')[:-1])
        self.ext = tmp.split('.')[-1]
        
    def directory(self:'path'):
        return  self.dir
    
    def nameFile(self:'str'):
        return self.name
    
    def extension(self:'str'):
        return self.ext
    
###############################################################################

class joinPath():

    def __init__(self, inPath='path', fileName=''):
        import os
        self.outputFile = os.path.join(inPath, fileName)
    
    def outFile(self:'path'):
        return self.outputFile
    
###############################################################################

class indexListPath():

    def __init__(self, listPath=['path'], index=0):
        
        self.outPath = listPath[index]
        
    def outPath(self:'path'):
        return self.outPath
    
###############################################################################

class indexArrayPath():

    def __init__(self, listPath=[['path']], index_row=0, index_col=0):
        
        self.outPath = listPath[index_row][index_col]
        
    def outPath(self:'path'):
        return self.outPath
    
###############################################################################

class ToListPath():

    def __init__(self, in_file='path'):
        
        self.outListPath = [in_file]
        
    def ListPath(self:'list_path'):
        return self.outListPath
    
###############################################################################

class build_list_path_dyn:
    def __init__(self,in_path='path',in_path_0='path',**dynamicsInputs):
        self.pathList = [in_path,in_path_0]
        for di in dynamicsInputs:
            self.pathList.append(dynamicsInputs[di])
    
    def path_list(self:'list_path'):
        return self.pathList
    
###############################################################################

class rstrip_path:
    def __init__(self, in_path='path', chr=''):
        self.outPath = in_path.rstrip(chr)
        
    def newPath(self:'path'):
        return self.outPath
     
