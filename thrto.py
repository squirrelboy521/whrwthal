#!/usr/bin/python3

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import Wthl
from Wthl import handler, io, parser, textile

# TODO: Implement PGP crytographic protection for all but ``main.py``,
# require passphrase on First-Use, don't require again as long as data
# is in namespace

# By convention, any method call of "self" will be self=Wthl
Wthl.__init__(Wthl)
gsize = Wthl.frame.grid_size()
for row in range(gsize[0]):
    Wthl.tk.Grid.rowconfigure(Wthl.frame, row, weight=1)
    for col in range(gsize[1]):
        Wthl.tk.Grid.columnconfigure(Wthl.frame, col, weight=1)
main = Wthl.tk.mainloop()
