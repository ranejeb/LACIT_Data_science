import StringIO, token, tokenize

prog_example="""for i in range(100): # comment

 if i % 1 == 0:

 print ":", t**2

"""
rl=StringIO.StringIO(prog_example).readline

for t_type, t_str, (br,bc), (er,ec), logl in tokenize.generate_tokens(rl):
    print ("%31 %10s : %20r" % (t_type, token.tok_name[t_type], t_str))