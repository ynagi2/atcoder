fun main() {
    var n = readLine()!!.toInt()
    if (n >= 42) {
        n++
    }
    println("AGC" + n.toString().padStart(3, '0'))
}
