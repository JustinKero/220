def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    total = 0
    numstudents = 0
    for line in infile:
        line_frag = line.split(":")
        student = line_frag[0]
        wg = line_frag[1].split()
        weightlst = []
        gradelst = []
        for i in range(0, len(wg)):
            wg[i] = int(wg[i])
        for j in range(0, len(wg), 2):
            weightlst.append(int(wg[j]))
            gradelst.append(int(wg[j+1]))
        nsum = 0
        for n in range(0, len(weightlst)):
            nsum = nsum + (weightlst[n] * gradelst[n])
        avg = nsum / 100
        avg = round(avg, 1)
        if sum(weightlst) == 100:
            outstring = str(student + "'s " + "average: " + str(avg))
            total = total + avg
            numstudents = numstudents + 1
        elif sum(weightlst) < 100:
            outstring = str(student + "'s " + "average: " + "Error: The weights are less than 100.")
        else:
            outstring = str(student + "'s " + "average: " + "Error: The weights are more than 100.")
        outfile.write(outstring + "\n")
    classavg = total / numstudents
    classavg = round(classavg, 1)
    totalstring = str(classavg)
    totalstring = str("Class average: " + totalstring)
    outfile.write(totalstring + "\n")


def main():
    weighted_average("grades.txt", "avg.txt")

main()