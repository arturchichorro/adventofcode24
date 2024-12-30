t_data = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

t1_data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

data = """x00: 1
x01: 1
x02: 0
x03: 0
x04: 0
x05: 1
x06: 0
x07: 1
x08: 1
x09: 0
x10: 1
x11: 0
x12: 0
x13: 1
x14: 1
x15: 1
x16: 0
x17: 0
x18: 1
x19: 1
x20: 1
x21: 0
x22: 1
x23: 1
x24: 0
x25: 0
x26: 0
x27: 1
x28: 1
x29: 0
x30: 0
x31: 0
x32: 0
x33: 1
x34: 0
x35: 1
x36: 0
x37: 0
x38: 1
x39: 1
x40: 0
x41: 0
x42: 0
x43: 0
x44: 1
y00: 1
y01: 0
y02: 1
y03: 1
y04: 0
y05: 0
y06: 1
y07: 1
y08: 0
y09: 1
y10: 1
y11: 1
y12: 1
y13: 1
y14: 1
y15: 1
y16: 0
y17: 1
y18: 1
y19: 0
y20: 0
y21: 1
y22: 1
y23: 1
y24: 0
y25: 0
y26: 0
y27: 0
y28: 0
y29: 1
y30: 0
y31: 1
y32: 1
y33: 1
y34: 1
y35: 0
y36: 1
y37: 0
y38: 1
y39: 0
y40: 1
y41: 1
y42: 1
y43: 1
y44: 1

rrq XOR tgf -> z26
x01 AND y01 -> dvp
y40 AND x40 -> vfn
dvp OR pct -> sbw
vws XOR rdp -> z33
bgt XOR tgv -> z14
ppv OR dhj -> pcn
y12 XOR x12 -> ndh
y12 AND x12 -> tnv
pkm AND cvq -> kbg
y04 AND x04 -> ktr
rbr XOR sbw -> z02
x42 XOR y42 -> skj
pkm XOR cvq -> vmv
mbg XOR fbw -> z39
fns OR hwk -> ggh
khb XOR nvn -> z43
x18 XOR y18 -> smg
tjf OR dqt -> khb
ggn XOR rkk -> z22
x18 AND y18 -> dtw
y10 XOR x10 -> dgr
x27 AND y27 -> bsj
jbq OR hds -> z20
x29 AND y29 -> qbs
cjv AND bgj -> grb
y22 AND x22 -> nws
y34 AND x34 -> krf
cpq OR fpm -> wnj
y28 XOR x28 -> vwh
y40 XOR x40 -> hnt
ndh XOR kws -> z12
y26 AND x26 -> vfd
dwh AND pcn -> rtt
y19 XOR x19 -> gvv
dtw OR vfp -> rbs
hkj XOR bmh -> z08
njf XOR ggh -> z16
x24 XOR y24 -> tpn
mkp AND vbj -> cwh
png OR vcv -> dhs
vfd OR mcw -> sbm
ssq AND skj -> dqt
dwj OR dsg -> hpj
x04 XOR y04 -> vvk
x20 XOR y20 -> bqn
smq OR qbs -> mdm
y06 XOR x06 -> kbj
rbr AND sbw -> nng
ndh AND kws -> vdc
y07 AND x07 -> z07
std AND vwp -> smq
y15 XOR x15 -> dgc
ggh AND njf -> djg
x30 AND y30 -> ppv
y39 XOR x39 -> fbw
x02 XOR y02 -> rbr
y42 AND x42 -> tjf
y03 AND x03 -> wqw
tqr XOR vkc -> z35
bbn XOR khs -> z41
rvr OR bfj -> tgf
y11 XOR x11 -> vkg
hkj AND bmh -> skt
x38 XOR y38 -> hkw
gqv XOR tkq -> z05
x38 AND y38 -> rjq
x00 AND y00 -> gjk
y09 XOR x09 -> mkp
y20 AND x20 -> hds
y17 XOR x17 -> bgj
pcn XOR dwh -> z31
x33 XOR y33 -> vws
x24 AND y24 -> pcc
y44 XOR x44 -> qcp
x29 XOR y29 -> vwp
y16 XOR x16 -> njf
mbg AND fbw -> qcm
kfm XOR jnb -> z21
qbd OR rjq -> mbg
y14 XOR x14 -> bgt
y02 AND x02 -> bwb
hpj XOR qcp -> z44
fnd AND hnt -> nvf
x22 XOR y22 -> rkk
hvc AND vkg -> wrp
pcc OR sns -> dqr
x37 AND y37 -> kqc
x26 XOR y26 -> rrq
tpf AND hkw -> qbd
mkp XOR vbj -> z09
vqs XOR wnj -> z37
rmq OR qrw -> cvq
ssq XOR skj -> z42
tkq AND gqv -> png
djg OR spn -> cjv
kfs XOR gfr -> z32
tgv AND bgt -> gjv
hqp OR qcm -> fnd
y25 XOR x25 -> phq
jsg XOR vwh -> hnv
vrm XOR sbm -> z27
y23 XOR x23 -> wfn
dqr AND phq -> rvr
nqs XOR wfn -> z23
y43 AND x43 -> dwj
y10 AND x10 -> smm
skt OR dvt -> vbj
x44 AND y44 -> bvd
hpj AND qcp -> vfw
y31 XOR x31 -> dwh
hcr OR hnv -> std
wbg OR rtt -> kfs
pbv OR stc -> rdp
wfn AND nqs -> vkh
y41 AND x41 -> fkv
dqr XOR phq -> z25
jww OR mnw -> tgv
mdm XOR gwh -> z30
fkv OR kdv -> ssq
hvc XOR vkg -> z11
trb AND sgw -> gbj
vwh AND jsg -> z28
y03 XOR x03 -> sgw
gms OR gjv -> nsh
tgf AND rrq -> mcw
nvf OR vfn -> khs
x09 AND y09 -> pss
khs AND bbn -> kdv
wdn XOR vtf -> z34
cgr XOR smg -> z18
x13 XOR y13 -> gnp
ffg OR kqc -> tpf
x25 AND y25 -> bfj
y06 AND x06 -> qrw
wrp OR bpk -> kws
khb AND nvn -> dsg
kvb OR tcq -> smh
kbj XOR dhs -> z06
mbk OR grb -> cgr
y39 AND x39 -> hqp
dgc AND nsh -> fns
x15 AND y15 -> hwk
x32 AND y32 -> stc
hth OR chh -> dkj
y41 XOR x41 -> bbn
wvv OR bsj -> jsg
x35 XOR y35 -> hth
y37 XOR x37 -> vqs
nng OR bwb -> trb
x28 AND y28 -> hcr
wdn AND vtf -> npt
x36 AND y36 -> cpq
y07 XOR x07 -> pkm
cbs AND gjk -> pct
tpn XOR ntn -> z24
vwp XOR std -> z29
wnj AND vqs -> ffg
kbj AND dhs -> rmq
smg AND cgr -> vfp
dkj AND vvp -> fpm
x08 XOR y08 -> bmh
kfm AND jnb -> mrb
gwh AND mdm -> dhj
y31 AND x31 -> wbg
x16 AND y16 -> spn
y43 XOR x43 -> nvn
nws OR wqr -> nqs
vmv OR kbg -> hkj
y23 AND x23 -> trq
vws AND rdp -> fvn
wqw OR gbj -> mwg
vfw OR bvd -> z45
cwh OR pss -> nvh
smh XOR bqn -> kfm
gvv XOR rbs -> z19
y08 AND x08 -> dvt
tnv OR vdc -> ffb
y00 XOR x00 -> z00
dgr AND nvh -> csw
vkc AND tqr -> chh
ggn AND rkk -> wqr
gjk XOR cbs -> z01
y14 AND x14 -> gms
x19 AND y19 -> tcq
dgr XOR nvh -> z10
vvp XOR dkj -> z36
x21 XOR y21 -> jnb
vvk AND mwg -> vdd
ffb XOR gnp -> z13
vvk XOR mwg -> z04
vkh OR trq -> ntn
rbs AND gvv -> kvb
sgw XOR trb -> z03
y33 AND x33 -> jkq
smh AND bqn -> jbq
x36 XOR y36 -> vvp
x34 XOR y34 -> vtf
ffb AND gnp -> mnw
x27 XOR y27 -> vrm
ntn AND tpn -> sns
smm OR csw -> hvc
y21 AND x21 -> vbc
y11 AND x11 -> bpk
vdd OR ktr -> tkq
y30 XOR x30 -> gwh
npt OR krf -> vkc
y32 XOR x32 -> gfr
y01 XOR x01 -> cbs
fvn OR jkq -> wdn
sbm AND vrm -> wvv
x35 AND y35 -> tqr
y13 AND x13 -> jww
gfr AND kfs -> pbv
dgc XOR nsh -> z15
vbc OR mrb -> ggn
x17 AND y17 -> mbk
y05 AND x05 -> vcv
tpf XOR hkw -> z38
cjv XOR bgj -> z17
x05 XOR y05 -> gqv
fnd XOR hnt -> z40"""

from collections import defaultdict

input = data

values = dict()
ops = []

for line in input.split("\n\n")[0].split("\n"):
    name, value = line.split(": ")
    values[name] = int(value)

for line in input.split("\n\n")[1].split("\n"):
    inp1, gate, inp2 = line.split(" ->")[0].split(" ")
    out = line.split("-> ")[1]
    ops.append((inp1, inp2, gate, out))

def work() -> int:
    global values
    missing = 0

    for (inp1, inp2, gate, out) in ops:
        if out in values: continue
        if inp1 not in values or inp2 not in values:
            missing += 1
            continue
            
        assert gate in ["AND", "OR", "XOR"], f"undefined gate {gate}"
        match gate:
            case "OR": values[out] = values[inp1] | values[inp2]
            case "AND": values[out] = values[inp1] & values[inp2]
            case "XOR": values[out] = values[inp1] ^ values[inp2]

    return missing

while work(): pass
output = 0
for k, v in values.items():
    if k[0] == "z": output |= v << int(k[1:])

print(output)

def get_path(wire: str) -> list:
    path = []
    for (inp1, inp2, gate, out) in ops:
        if out == wire:
            path.append((inp1, inp2, gate, out))
            path += get_path(inp1)
            path += get_path(inp2)

    return path

def highest_bit(n: int) -> int | None:
    if not n: return None
    bit = 0
    while n:
        n >>= 1
        bit += 1
    return bit-1

last_output = f"z{highest_bit(output)}"
print(f"highest bit is {last_output}")

usage = defaultdict(set)
errors = []

for (inp1, inp2, gate, _) in ops:
    usage[inp1].add(gate)
    usage[inp2].add(gate)

for (inp1, inp2, gate, out) in ops:
    if out == last_output:
        if inp1[0] == "x" or inp1[0] == "y" or inp2[0] == "x" or inp2[0] == "y" or gate != "OR":
            errors.append(out)
        continue

    if out == "z00":
        if sorted([inp1, inp2]) != ["x00", "y00"]: errors.append(out)
        if gate != "XOR": errors.append(out)
        continue

    if inp1 == "x00" or inp1 == "y00" or inp2 == "x00" or inp2 == "y00":
        if (inp1[0] == "x" and inp2[0] == "y") or (inp1[0] == "y" and inp2[0] == "x"):
            if gate != "XOR" and gate != "AND": errors.append(out)
        continue

    if gate == "XOR":
        if inp1[0] == "x" or inp1[0] == "y":
            if inp2[0] != "x" and inp2[0] != "y": errors.append(out)
            if out[0] == "z": errors.append(out)
            if "AND" not in usage[out] or "XOR" not in usage[out]:
                errors.append(out)
        elif out[0] != "z": errors.append(out)
    
    elif gate == "OR":
        if inp1[0] == "x" or inp1[0] == "y" or inp2[0] == "x" or inp2[0] == "y" or out[0] == "z":
            errors.append(out)
        if "AND" not in usage[out] or "XOR" not in usage[out]:
            errors.append(out)
    
    elif gate == "AND":
        if inp1[0] == "x" or inp1[0] == "y":
            if inp2[0] != "x" and inp2[0] != "y": errors.append(out)
        if "OR" not in usage[out]:
            errors.append(out)

errors = sorted(list(set(errors)))
assert len(errors) == 8, f"expected 8 values but got {len(errors)}"

for i in range(len(errors)):
    if i == len(errors)-1: print(errors[i])
    else: print(errors[i], end=",")