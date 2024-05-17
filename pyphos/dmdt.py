import types
import lib_aesgcm
import lib_phos

import readline
import glob
import json
import os
import getpass
import base64
import traceback

# 2021-01-17 disable for debugging
# import lib_chrome
# browser = lib_chrome.browser
# driver  = browser

# print('  2021-01-17' )

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
  # print( '  SM token list t ', t )
  L = len(t)
  i = 0
  while i<L:
    t_i = i
    if ( t[i][-1]==':'):
      Lt=len(t[i])
      # print( 'is :', 'f_'+t[i][0:Lt-1])
      tf = 'f_'+t[i][0:Lt-1]
      
      if tf in dir(lib_aesgcm): # check tf in lib first, else globals() will not be able to find function defition in global
        print( tf, ' is defined')
        eval( 'lib_aesgcm.'+tf+'()' ) 
        
      elif (tf=='f_newtab'):
        print('  hard code execute_script ')
        driver.execute_script("window.open('"+ S.pop() +"')") # too complicated to eval quotes !!
      
      # elif tf in dir(lib_chrome): # check tf in lib manually, until too many, automate all
      #  print( tf, ' is defined')
      #  eval( 'lib_chrome.'+tf+'()' ) 
      
      elif 'f_'+t[i][0:Lt-1] in globals().keys():
        # print( 'f_'+t[i][0:Lt-1], ' is defined')
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
    print('  SM i ', i,'  L ',L, '  t ', t)
    i += 1

T=[]
VC=0
def SM_n(s):  # nested SM use T
  s1 = " ".join(s.split())
  global t, t_i, VC
  t = s1.split()
  
  # print( '  SM_n t_i in vars()', 't_i' in vars() )
  
  if (len(T)==0):
    # if ('t_i' in vars()):
    #  print('  t_i ',t_i)
  # else:
    t_i = 0
  
  # if ('i' in vars()):
  #  print('  i ',i)
    
  # if (not ('t_i' in vars())):
  #  t_i = 0

  T.append([t,t_i]); VC += 1;
  # print( '\n\n  SM token array VC T ', VC, T )
  L = len(t)
  i = 0
  while i<L and VC<5:
    t_i = i  # i = t_i at end of loop caused i to be referenced to t_i, no longer local variable?
    # print( '  SM_n while start t_i in vars()', 't_i' in vars() )
    # print( '\n  SM_n while start t_i VC ', t_i, VC, T )
    # traceback.print_stack()
    if ( t[i][-1]==':'):
      Lt=len(t[i])
      # print( 'is :', 'f_'+t[i][0:Lt-1])
      tf = 'f_'+t[i][0:Lt-1]
      
      if tf in dir(lib_aesgcm): # check tf in lib first, else globals() will not be able to find function defition in global
        print( tf, ' is defined')
        eval( 'lib_aesgcm.'+tf+'()' ) 
        
      elif (tf=='f_newtab'):
        print('  hard code execute_script ')
        driver.execute_script("window.open('"+ S.pop() +"')") # too complicated to eval quotes !!
      
      # elif tf in dir(lib_chrome): # check tf in lib manually, until too many, automate all
      #  print( tf, ' is defined')
      #  eval( 'lib_chrome.'+tf+'()' ) 
      
      elif 'f_'+t[i][0:Lt-1] in globals().keys():
        # print( 'f_'+t[i][0:Lt-1], ' is defined')
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
    # parent function resumes here after child finishes !!
    
    '''
    if (i<len(t)):
      print('  END SM_n i ', i, '  t_i',t_i,'  t[i] ',t[i], '  L ',L, '  t ', t)
    else:
      break
    '''
    # print('  SM_n while end t_i in vars()', 't_i' in vars() )
    i += 1
    
  t_i=T.pop()[1]+1; # VC -= 1;
  
  if (len(T)>0): 
    t=T[-1][0]; # i=T[-1][1];
  else:
    return
  
  #print('  i ',i, '  t_i ',t_i,'  L ',len(t),(i>=len(t)),'  t ',t,'  T ', len(T), T)
  '''
  if (i>=len(t)):
    print('  should stop ?? T ', T)
    traceback.print_stack()
    # break
    return
  '''
  
f=SM_n
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
  
# SM("pvk.txt fi:")
# print(S)
# print( globals().keys() )
# print( dir( lib_aesgcm ) )

'''
for key in list(globals().keys()):   # iter on both keys and values
        if key.startswith('lib_'):
                print( key )
'''

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
from operator import imul
import datetime

vk=lib_aesgcm.RSA.generate(1024)
seed=0

def f_path(): # path safe b64
  a = s.pop();
  if (a.find('/')>=0):
    a=a.replace('/', '_')
  if (a.find('/')>=0):
    a=a.replace('+', '-')
  s.append(a)

def bnToB64(bn):
  # var hex = BigInt(bn).toString(16);
  hn = hex(bn); # return hn;
  # if (hex.length % 2) { hex = '0' + hex; }
  if len(hn)%2:
    hn=hn[:2]+'0'+hn[2:]
    # print("need 0", hn)
  bin = [];
  i = 2;
  while (i < len(hn)):
    # print(hn[2:4], int(hn[2:4],16), chr(int(hn[2:4],16)))
    # print(hn[i:i+2], int(hn[i:i+2],16), chr(int(hn[i:i+2],16)))
    # b=chr(int(hn[i:i+2],16))
    b=int(hn[i:i+2],16)
    bin.append(b);
    i = i + 2
  return bin

def urs13(h):
  return (h>>13) if h>0 else int(bin(h^0xFFFFFFFF)[3:22],2)

def urs16(h):
  return (h>>16) if h>0 else int(bin(h^0xFFFFFFFF)[3:19],2)

def imul(a,b):
  c=(a*b)%pow(2,32)
  if c >= pow(2,31):
    return c-pow(2,32)
  else:
    return c

def h53(v1):
	h1 = 0xdeadbeef ^ seed; h2 = 0x41c6ce57 ^ seed;
	for i in range(len(v1)):
	  ch = ord(v1[i])
	  h1 = imul(h1 ^ ch, 2654435761);
	  h2 = imul(h2 ^ ch, 1597334677);
	  # print(i, v1[i], ord(v1[i]), h1, h2)
	h1 = imul(h1 ^ urs16(h1), 2246822507) ^ imul(h2 ^ urs13(h2), 3266489909);
	h2 = imul(h2 ^ urs16(h2), 2246822507) ^ imul(h1 ^ urs13(h1), 3266489909);
	# print(h1,h2)
	return 4294967296 * (2097151 & h2) + (h1>>0);

def mkjson():
	s.append({'t': str(datetime.datetime.now()) })
	s.append( { 'name': 'Adam' } )
	print('Your name is '+ s[-1]['name'] +' by default. Please modify the program accordingly.')
	s[-1].update(s[-2])
	print('Please enter the URL of the source code that you downloaded:')
	s.append(input())
	s.append( {'u': s[-1] } )
	del(s[-2])
	s[-1].update(s[-2])
	s.append( base64.b64encode(bytearray(bnToB64(h53(str(vk.public_key().exportKey('PEM')))))) )
	s[-1].decode('utf-8')
	s.append(s[-1].decode('utf-8'))
	f_path()
	del(s[-2])
	s.append( {'h': s[-1]} )
	del(s[-2])
	s[-1].update(s[-2])
	s.append( json.dumps( s[-1] ) )
	s.append(base64.b64encode(bytearray(bnToB64(h53(s[-1])))))
	s.append(s[-1].decode('utf-8'))
	f_path()
	del(s[-2])
	s.append('Graph/hg/'+s[-1])
	print('JSON string is saved at '+s[-1])
	del(s[-2])
	f_wl()

def f_dt():
  s.append(str(datetime.datetime.now()))

def f_hpbk():
  s.append( base64.b64encode(bytearray(bnToB64(h53(str(vk.public_key().exportKey('PEM')))))) )

def f_du8():
  s.append(s.pop().decode('utf-8'))

def f_je():
  s.append( json.dumps( s.pop() ) )

def f_hbp(): # h53: base64() path:
  s.append(base64.b64encode(bytearray(bnToB64(h53(s.pop())))))
  f('du8: path:')

def f_hgf(): # hash graph file
  s.append('Graph/hg/'+s.pop())

def f_mkjson(): # Phoscript version of mkjson
	# s.append({'t': str(datetime.datetime.now()) })
	f('dt: t mo:')
	# s.append( { 'name': 'Adam' } )
	f('Adam name mo:')
	print('Your name is '+ s[-1]['name'] +' by default. Please modify the program accordingly.')
	# s[-1].update(s[-2])
	f('u:')
	print('Please enter the URL of the source code that you downloaded:')
	# s.append(input())
	f('in:')
	# s.append( {'u': s[-1] } )
	# del(s[-2])
	# s[-1].update(s[-2])
	f('u mo: u:')
	# s.append( base64.b64encode(bytearray(bnToB64(h53(str(vk.public_key().exportKey('PEM')))))) )
	f('hpbk:')
	# s[-1].decode('utf-8')
	# s.append(s[-1].decode('utf-8'))
	f('du8:')
	# f_path()
	f('path:')
	# del(s[-2])
	# s.append( {'h': s[-1]} )
	# del(s[-2])
	# s[-1].update(s[-2])
	f('h mo: u:')
	# s.append( json.dumps( s[-1] ) )
	f('dup: je:')
	# s.append(base64.b64encode(bytearray(bnToB64(h53(s[-1])))))
	# s.append(s[-1].decode('utf-8'))
	# f_path()
	# del(s[-2])
	f('dup: hbp:')
	# s.append('Graph/hg/'+s[-1])
	print('JSON string is saved at Graph/hg/'+s[-1])
	# del(s[-2])
	# f_wl()
	f('hgf: wl:')

def f_dmdt(): # clean up of Phoscript version of mkjson
	f('dt: t mo:')
	f('Adam name mo:')
	print('Your name is '+ s[-1]['name'] +' by default. Please modify the program accordingly.')
	f('u:')
	print('Please enter the URL of the source code that you downloaded:')
	f('in:')
	f('u mo: u:')
	f('hpbk:')
	f('du8:')
	f('path:')
	f('h mo: u:')
	f('dup: je:')
	f('dup: hbp:')
	print('JSON string is saved at Graph/hg/'+s[-1])
	f('hgf: wl:')

def f_dmdt_s(): # SHORT clean up of Phoscript version of mkjson
	f('dt: t mo: Adam name mo: u:')
	print('Your name is '+ s[-1]['name'] +' by default. Please modify the program accordingly.')
	print('Please enter the URL of the source code that you downloaded:')
	# f('in: u mo: u: hpbk: du8: path: h mo: u: dup: je: dup:')
	# f_hbp()
	f('in: u mo: u: hpbk: du8: path: h mo: u: dup: je: dup: hbp:')
	print('JSON string is saved at Graph/hg/'+s[-1])
	f('hgf: wl:')

