
import java.awt.Color;

/**
 * snake
 */
public class snake {

    // private final int B_WIDTH=300;
    // private final int B_HEIGHT=300;
    // private final int DOT_SIZE=10;
    // private final int ALL_DOTS=300;
    // private final int RAND_POS=29;
    // private final int delay=140;
    
    // private final int x[]=new int[ALL_DOTS];
    // private final int y[]=new int[ALL_DOTS];

    // private int dots;
    // private int apple_x;
    // private int apple_y;

    static final int SCREEN_SIZE_X=40
    static final int SCREEN_SIZE_Y=40

    final int MAX_SNAKE_LENGTH = 1000;

    int SNAKE_LENGTH[] snakeSecs=new SnakeSection{MAX_SNAKE_LENGTH];
    int dirX=-1;
    int dirY=0;

    Color color;

    public Snake(Snakesection startpos,int dx,int dy,color color){
        for(int i=0,i<MAX_SNAKE_LENGTH,i++)
        Snakesec[]=new SnakeSection(0,0);
    }
} 