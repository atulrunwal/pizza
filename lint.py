#!/usr/bin/env python
# coding: utf-8

# In[2]:


#lint.py 

import sys 

from pylint import lint  

THRESHOLD = -7

run = lint.Run(["exercise4.py"], do_exit=False) 

score = run.linter.stats["global_note"]  

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 


# In[ ]: