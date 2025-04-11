class circle(val radius:Double) {
    constructor(name: String): this(1.0)
    constructor(diametr: Int) : this(diametr/2.0)
    {
        println("in diametr")
    }
    init {
        println("1")
    }
    init {
        println("2")
    }
}
fun main(){
    val circle1 = circle(5.0)
    val circle2 = circle("string")
}