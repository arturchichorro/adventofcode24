data = """
...............3................d.................
.........................s..7......i.....e........
................C.......................e.........
...............Z.......m....................e.....
....................gC.....q......................
...............Q....s..........................A..
................................s........A........
...........n.....3.C..F......w..m...d.............
..E...............3.....m......d.i................
............f.3.......C....d........A.............
.........Z...........................n..A.........
....Q......p..............g.i.....................
.r......n...Q....p............S.7...........O.....
..........r......K....p.....M..........7....G.....
....................Fs...................G........
..z.........D..........G.g........................
rR.............F................M...............G.
.........I..c.nr...............M................O.
...I..............................................
...................f......I.......................
z.I...............f..K..........0................7
k...................K......u.........O............
.........Q...z.................ga......0.......o..
....E.5..F..................u..b.P......a.1.......
..........k9..................K.........H......1..
.E.........h..........................0......a...H
..........9...h..e........i......M....1...........
.c.............z.......................j.........T
c..D......................Pb.................2....
....................w.y......W......j.........T.2.
......ph...N..................y.......W.t.2.......
............9.................................o..1
.................Vq.......u....Pb.................
.......6R.........................................
........5............w...a.W.............H.j......
......Z.......Y..........V............H..2........
..........D.................v..y.........t...T..o.
.......5...................t......................
........8k...l...............v.........S....T...4.
......6....U......PR........b.B....y..............
..........6.V...U........................L........
.......8.........N....4.Vq.v..t......oJ.....L.....
N...........R.................w.JY................
............N.....................................
.....5Y.....................................j.....
.98........Y.....l.............B...........S...L..
.8...............U...............4................
..................W.........U4....................
...E........l..........B......................L..u
.....D............l....J..q.....................S."""

t_data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

matrix = [list(line) for line in data.strip().split("\n")]

rows, cols = len(matrix), len(matrix[0])

antenna_pos_dict = {}
antinode_positions = set()

for row in range(rows):
    for col in range(cols):
        char = matrix[row][col]
        if char.isalnum():
            if char not in antenna_pos_dict:
                antenna_pos_dict[char] = []
            antenna_pos_dict[char].append((row, col))


def subtrack_tuple(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

for char, positions in antenna_pos_dict.items():
    
    for i in range(len(positions)):
        for j in range(len(positions)):

            if i != j:
                dist = subtrack_tuple(positions[j], positions[i])

                prev_node =  subtrack_tuple(positions[i], dist)
                if prev_node[0] >= 0 and prev_node[0] < rows and prev_node[1] >= 0 and prev_node[1] < cols:
                    antinode_positions.add(prev_node)

                after_node = add_tuple(positions[j], dist)
                if after_node[0] >= 0 and after_node[0] < rows and after_node[1] >= 0 and after_node[1] < cols:
                    antinode_positions.add(after_node)


print(len(antinode_positions))

