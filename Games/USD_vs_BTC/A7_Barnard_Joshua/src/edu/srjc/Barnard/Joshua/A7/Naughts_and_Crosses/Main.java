/*
Joshua P. Barnard
jpb68@humboldt.edu
03/28/2018
Naughts and Crosses
CS 17.11

This is an interactive 2-player game based on tic-tac-toe where the first player to form a line of 3 of their tokens,
they win.  If the board fills up before any player is able to form a line of three then the game is a draw, or "Cat's Game".
 */


package edu.srjc.Barnard.Joshua.A7.Naughts_and_Crosses;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application
{

    @Override
    public void start( Stage stage ) throws Exception
    {
        Parent root = FXMLLoader.load( getClass().getResource("GameUI.fxml" ) );

        Scene scene = new Scene( root );

        stage.setTitle( "BitCoin vs US Dollar" );
        stage.setScene( scene );
        stage.setResizable( false );
        stage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        launch(args);
    }

}

