### Maldoc
simple script to generate a macro enabled payload.
### Usage:
`python3 gen_ps.py <host_IP> PORT`
- If you are conserned with the size of the payload, then do the following .
- Edit the python file named `format_ps.py` and add the newly generated payload from 1-) . Then run the following :
`python3 format_ps.py`
- You will have a `<=50` character per line payload created in a file called `payload.txt`.
