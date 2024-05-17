import types
import lib_aesgcm
import lib_phos

import readline
import glob
import json
import os
import getpass
import base64

# 2021-01-17 disable for debugging
import lib_chrome
browser = lib_chrome.browser
driver  = browser

print('  2021-01-17' )

def f_ytdl():
  os.system('./Graph/bin/youtube-dl '+ S.pop() )

def f_mp3(): # extract mp3 from video
  f_o = S.pop()
  C='ffmpeg -i '+ S.pop() +' '+ f_o
  os.system( C )

def f_b64e():
  S.append( base64.b64encode( S.pop() ) )

def f_b64d():
  S.append( base64.b64decode( S.pop() ) )

def f_h():
  S.append('\n'.join( [ str(readline.get_history_item(i + 1)) for i in range( readline.get_current_history_length() ) ] ) )

def f_pw():
  S.append( getpass.getpass() )
  
def f_swap():
  a=S.pop()
  b=S.pop()
  S.append(a)
  S.append(b)

def h():
  print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))

def f_dup():
  S.append( S[-1] )

# 20230602
# def f_fi(): # WAS php fgc !!
def f_fi_xnl(): # remove newline
  S.append(open(S.pop()).read().split("\n"))

def f_fi(): # put back newline as in PHP
  S.append(open(S.pop()).read().split("\n"))  # .__add__("\n"))
  b=S.pop()
  d=[]
  for c in b:
    if (len(c)>0): 
      d.append(c+"\n")
  S.append(d)

def f_fgc(): # is php fgc !!
  S.append(open(S.pop()).read())

def f_len():
  S.append(len(S.pop()))

def f_split(): # string.split
  c=S.pop()
  S.append( S.pop().split(c) )

def f_m1w(): # merge 1 word to string
  w = S.pop()
  S.append( S.pop() + w )


# S.append(['X', 'who_is', 'Y'])  ## input must be list, then f('mmn:')
def f_mmn(): # multi level make node
  N = S.pop()
  i = 0
  P = 'Graph' # parent
  for n in N:
    print(n, S)
    # if (i>=2 and i<=5):
    if (i>=0):
      SM('5566 link '+ n +' mn: '+ P +' wn:')
      print(P)
      P = P +'/'+ n
      S.pop()
      # break
    i += 1
  S.append(P)
  
# 'f_fi' in globals().keys()

def f_lib():
  for key in list(globals().keys()):   
    if key.startswith('lib_'):
        print( key )
        S.append( key )

def f_dir():
  M = eval( S.pop() )
  print( M )
  S.append( dir( M ) )  # eval( "lib_*" ), result was string, must add eval !!

def f_startswith():
  ks = S.pop()
  L  = S.pop()
  for key in L:   
    if key.startswith( ks ):
        print( key )
        S.append( key )

def f_sw(): # alias
  f_startswith()

def f_pick():
  n = int( S.pop() )
  S.append( S[-n-1] )
  
def f_glob():
  #files = glob.glob('Graph/**/*', recursive = True) 
  p = S.pop()
  if p == '*':  
    S.append( glob.glob('Graph/**/*', recursive = True) ) 
  elif p[0] == '/':
    S.append( glob.glob( p+'/*' ) ) 
  else:
    S.append( glob.glob('Graph/'+p+'/**/*', recursive = True) ) 
  
def f_grep():
  k = S.pop()
  S.append( [name for name in S.pop() if k in name] )
  
def f_mn(): # make node
  # {'name': 'p_Adam', 'role': 'person', 'pbk': '1221'}
  # x = '{"name": "'+ S.pop() +'", "role": "'+ S.pop() +'", "pbk": "'+ S.pop() +'"}'
  x = '{"name": "'+ str(S.pop()) +'", "role": "'+ str(S.pop()) +'", "pbk": "'+ str(S.pop()) +'"}'
  # print(x)
  S.append( json.loads(x) )

# function fgl_wn() // array dirname wn: write node to files (paths)
def f_wn():
    if type( S[-1] ) == str:
      G = S.pop()+'/'
    else:
      G = "Graph/";  # must set Parent !!
    N = S[-1]
    print( '  in wn: N ', N )
    D = G+N['name'] 
    if not os.path.exists( D ):
      os.mkdir( D )   
    for k in N:
      with open(D+'/'+k, 'a') as the_file:
        the_file.write(N[k])


def f_wl(): # write leave node
      with open(S.pop(), 'a') as the_file:
        the_file.write(S.pop())        

# S = []
S = lib_phos.S
LIB = lib_phos.LIB
s=S  # alias compatible with JavaScript Phos


# 20230602 global t; map need to access t
def SM(s):  
  s1 = " ".join(s.split())
  global t, t_i
  t = s1.split()
  print( '  SM token list t ', t )
  L = len(t)
  i = 0
  while i<L:
    t_i = i
    if ( t[i][-1]==':'):
      Lt=len(t[i])
      print( 'is :', 'f_'+t[i][0:Lt-1])
      tf = 'f_'+t[i][0:Lt-1]
      
      if tf in dir(lib_aesgcm): # check tf in lib first, else globals() will not be able to find function defition in global
        print( tf, ' is defined')
        eval( 'lib_aesgcm.'+tf+'()' ) 
        
      elif (tf=='f_newtab'):
        print('  hard code execute_script ')
        driver.execute_script("window.open('"+ S.pop() +"')") # too complicated to eval quotes !!
      
      elif tf in dir(lib_chrome): # check tf in lib manually, until too many, automate all
        print( tf, ' is defined')
        eval( 'lib_chrome.'+tf+'()' ) 
      
      elif 'f_'+t[i][0:Lt-1] in globals().keys():
        print( 'f_'+t[i][0:Lt-1], ' is defined')
        eval( 'f_'+t[i][0:Lt-1]+'()' )
      
      elif tf in LIB.keys():
        print( tf, ' is in ', LIB[tf] )
    elif (t[i]=='f'):
      turtle.forward( S.pop() )
    elif (t[i]=='l'):
      turtle.left( S.pop() )
    elif isinstance(t[i], float):
      S.append( float(t[i]) )
    elif t[i].lstrip("-+").isdigit(): # check if digit
      S.append( int(t[i]) )
    elif t[i]=='+':
      S.append( S.pop() + S.pop() )
    elif t[i]=='-':
      S.append( - S.pop() + S.pop() )
    else:
      S.append( t[i] )
    i = t_i # f_map etc loop like function will modify t_i
    i += 1

f=SM
# s=S

# 20230602
# f("h_1840 fi: array: map: len:")
def f_map():
  global t, t_i, s
  a=s[-2]
  b=s[-1]
  # print(t_i, t, s, a, b)
  i=t_i+1
  Lt=len(t[i])
  if 'f_'+t[i][0:Lt-1] in globals().keys():
    for c in a:
      s.append(c)
      print( 'f_'+t[i][0:Lt-1], ' is defined. c ', c)
      eval( 'f_'+t[i][0:Lt-1]+'()' )
      b.append(s.pop())
  t_i += 1
  # a=S.pop()
  # S.append(map(S.pop()))
  # S.append(len(S.pop()))
  
def f_s():
  print(S)

def f_array():
  S.append([])
    
def f_i():
  # n = int(S.pop())
  n = (S.pop())
  S.append( S.pop()[ n ] )
  
def f_ix(): # i element of list (array) no pop
  n = (S.pop())
  S.append( S[-1][ n ] )
  
  
def is_int(val):
   return val.lstrip("-+").isdigit()

# must not have 2 line breaks, will stop function def in interpreter mode
  
SM("pvk.txt fi:")
print(S)

print( globals().keys() )
print( dir( lib_aesgcm ) )


for key in list(globals().keys()):   # iter on both keys and values
        if key.startswith('lib_'):
                print( key )

tab_phos = ''

# 11. windows_before = driver.current_window_handle
def f_tab_phos():
    global tab_phos # without global, cannot write to global var tab_phos
    driver=browser
    windows_before = driver.current_window_handle
    tab_sn = windows_before
    u_phos='http://192.168.43.119/2021/Phosway/duix/phoshell.php?a'
    driver.execute_script("window.open('"+ u_phos +"')")
    windows_after = driver.window_handles
    tab_phos = [x for x in windows_after if x != windows_before][0]
    driver.switch_to.window(tab_phos)

# 12. print link in web page,
# appendChild to body
# f_tabs()
def f_ac_url():
    SM('utabs:')
    driver.switch_to.window(tab_phos)
    JS_AC = "window.f_appc = function( s ) { var body=document.getElementsByTagName('body')[0]; var B=document.createElement('div'); B.innerHTML=s; body.appendChild(B); }"
    driver.execute_script( JS_AC )
    SM('0 ix: ac:')
    SM('1 ix: ac:')
    SM('2 ix: ac:')
    SM('===== ac:')
    SM('===== ac:')
    S.append('Click PHOS to write URLs to Graph Database')
    SM('ac:')

# 13. click phos,  write to Graph
def f_wg():   
  for x in [0, 1, 2]:
    print(x)
    S.append(x)
    SM('ix:')
    SM('dup:')
    SM('/ split:')
    SM("dup: mmn:")
    SM('/val m1w:')
    SM('dup: 3 pick:')
    SM('swap: wl:')
    SM('fi:')
    S.pop()
    S.pop()
    S.pop()

def f_wait_wg():
    driver.switch_to.window(tab_phos)
    lib_chrome.wait_alert(browser)
    f_wg()
    
def f_phos_wg():
    f_tab_phos()
    f_ac_url()
    f_wait_wg()
    
def f_es():
    driver.execute_script( S.pop() )
    
def f_j_geid():
    S.append( "document.getElementById('"+ S.pop() +"')" )    
    
def f_j_getn():
    S.append( "document.getElementsByTagName('"+ S.pop() +"')" )        

def f_j_gecn():
    S.append( "document.getElementsByClassName('"+ S.pop() +"')" )        
    
def f_j_i():
    i = str(S.pop())
    print(i, type(i))
    S.append( S.pop()+"["+i+"]" )
    
def f_j_cc(): # children chain
    n = (S.pop())
    x=0
    CC=""
    while x<n:
        i = str(S.pop())
        print(i, type(i))
        CC+=".children["+i+"]"  
        x+=1   
    S.append( S.pop() + CC )
    
def f_j_it():
    S.append( S.pop()+".innerText")
    
def f_j_eq():
    S.append( S.pop()+"=" )
    
def f_j_sq(): # single quote
    S.append( "'"+S.pop()+"'")
    
def f_j_dq(): # double quote
    S.append( '"'+S.pop()+'"')    
    
def f_jstr(): # join two strings
    sa=S.pop()
    S.append( S.pop() + sa )
    
def f_in():
  s.append(input())

def f_u():
  a=s.pop()
  a.update(s.pop())
  s.append(a)
  
def f_mo():
  s.append({s.pop():s.pop()})

from dill.source import getsource
