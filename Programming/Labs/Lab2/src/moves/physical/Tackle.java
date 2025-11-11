package moves.physical;
import ru.ifmo.se.pokemon.*;

public class Tackle extends PhysicalMove {
    public Tackle() {
        super(Type.NORMAL, 40, 0.1);
    }

    @Override
    protected String describe() {
        return "uses Tackle";
    }
}
