package moves.physical;
import ru.ifmo.se.pokemon.*;

public class TakeDown extends PhysicalMove {
    public TakeDown() {
        super(Type.NORMAL, 90, 0.85);
    }

    @Override
    protected void applySelfDamage(Pokemon att, double damage) {
        att.setMod(Stat.HP, (int) Math.round(damage / 4));
    }

    @Override
    protected String describe() {
        return "uses Take Down with recoil damage";
    }
    
}
