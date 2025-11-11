package moves.special;
import ru.ifmo.se.pokemon.*;

public class BubbleBeam extends SpecialMove {
    public BubbleBeam() {
        super(Type.WATER, 65, 0.1);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.1) {
            p.setMod(Stat.SPEED, -1);
        }
    }

    @Override
    protected String describe() {
        return "uses Bubble Beam";
    }
}
