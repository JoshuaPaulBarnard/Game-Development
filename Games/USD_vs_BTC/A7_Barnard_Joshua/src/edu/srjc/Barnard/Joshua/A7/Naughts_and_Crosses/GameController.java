/*
Joshua P. Barnard
jpb68@humboldt.edu
03/28/2018
Naughts and Crosses
CS 17.11

This is main code for the bitcoin vs us dollar tic-tac-toe game.
*/

package edu.srjc.Barnard.Joshua.A7.Naughts_and_Crosses;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;


public class GameController implements Initializable
{

    @FXML
    private GridPane gameGrid;

    private Image blankImage;
    private Image usdImage;
    private Image btcImage;

    private enum Players
    {
        USD,
        BTC,
        None
    }

    Players[][] gameBoard = new Players[3][3];

    Players whoseTurn = Players.USD;

    @Override
    public void initialize(URL url, ResourceBundle rb)
    {
        blankImage = new Image("images/blank.png");
        usdImage = new Image("images/usd.png");
        btcImage = new Image("images/btc.png");


        for (int i = 0; i < gameGrid.getColumnCount(); i++)
        {
            for (int j = 0; j < gameGrid.getRowCount(); j++)
            {
                gameBoard[i][j] = Players.None;

                ImageView img = new ImageView();
                img.setImage(blankImage);
                img.setFitWidth(195);
                img.setFitHeight(195);
                img.setPreserveRatio(true);
                img.setSmooth( true );
                img.setCache( true );
                img.setId(String.format("image%s%s", i, j));

//                img.setOnMouseClicked(new EventHandler<MouseEvent>()
//                {
//                    @Override
//                    public void handle(MouseEvent event)
//                    {
//                        imgview_Clicked(event);
//                    }
//                });

                img.setOnMouseClicked(event -> {
                    imgview_Clicked(event);
                });
                gameGrid.add(img, i,j);
            }
        }
        gameGrid.setGridLinesVisible(true);

    }


    private void imgview_Clicked(MouseEvent e)
    {
        ImageView img = (ImageView)e.getSource();
        img.setFitWidth(195);
        img.setFitHeight(195);
        img.setPreserveRatio(true);
        img.setSmooth( true );
        img.setCache( true );
        int row = Integer.parseInt(img.getId().substring(5,6));
        int col = Integer.parseInt(img.getId().substring(6));

        if (gameBoard[row][col] == Players.None)
        {
            if (whoseTurn == Players.USD)
            {
                img.setImage(usdImage);
                whoseTurn = Players.BTC;
                gameBoard[row][col] = Players.USD;
            }
            else
            {
                img.setImage(btcImage);
                whoseTurn = Players.USD;
                gameBoard[row][col] = Players.BTC;
            }
        }
        else
        {
            if( gameBoard[0][0] != Players.None && gameBoard[0][1] != Players.None && gameBoard[0][2] != Players.None &&
                    gameBoard[1][0] != Players.None && gameBoard[1][1] != Players.None && gameBoard[1][2] != Players.None &&
                    gameBoard[2][0] != Players.None && gameBoard[2][1] != Players.None && gameBoard[2][2] != Players.None )
            {
                Alert alert = new Alert(Alert.AlertType.WARNING);
                alert.setHeaderText(null);
                alert.setContentText( "Cat's Game." );
                alert.showAndWait();
//              alert.show();
            }
            else
            {
                Alert alert = new Alert(Alert.AlertType.WARNING);
                alert.setHeaderText(null);
                alert.setContentText("That is already taken.");
                alert.showAndWait();
//              alert.show();
            }

        }


    }


    public void mechanisms(  ) throws Exception
    {
        if( gameBoard[0][0] != Players.None && gameBoard[0][1] != Players.None && gameBoard[0][2] != Players.None &&
                gameBoard[1][0] != Players.None && gameBoard[1][1] != Players.None && gameBoard[1][2] != Players.None &&
                gameBoard[2][0] != Players.None && gameBoard[2][1] != Players.None && gameBoard[2][2] != Players.None )
        {
            throw new Exception( "Cat's Game" );
        }

        if( ( gameBoard[0][0] == Players.USD && gameBoard[0][1] == Players.USD && gameBoard[0][2] == Players.USD )  ||
                ( gameBoard[0][0] == Players.USD && gameBoard[1][1] == Players.USD && gameBoard[2][2] == Players.USD ) ||
                ( gameBoard[0][0] == Players.USD && gameBoard[1][0] == Players.USD && gameBoard[2][0] == Players.USD ) ||
                ( gameBoard[1][0] == Players.USD && gameBoard[1][1] == Players.USD && gameBoard[1][2] == Players.USD ) ||
                ( gameBoard[2][0] == Players.USD && gameBoard[1][1] == Players.USD && gameBoard[0][2] == Players.USD ) ||
                ( gameBoard[2][0] == Players.USD && gameBoard[2][1] == Players.USD && gameBoard[2][2] == Players.USD ) ||
                ( gameBoard[0][1] == Players.USD && gameBoard[1][1] == Players.USD && gameBoard[2][1] == Players.USD ) ||
                ( gameBoard[0][0] == Players.USD && gameBoard[1][0] == Players.USD && gameBoard[2][0] == Players.USD ) ||
                ( gameBoard[0][2] == Players.USD && gameBoard[1][2] == Players.USD && gameBoard[2][2] == Players.USD ) )
        {
            throw new Exception( "Player 1 (USD) Wins!" );
        }

        if( ( gameBoard[0][0] == Players.BTC && gameBoard[0][1] == Players.BTC && gameBoard[0][2] == Players.BTC )  ||
                ( gameBoard[0][0] == Players.BTC && gameBoard[1][1] == Players.BTC && gameBoard[2][2] == Players.BTC ) ||
                ( gameBoard[0][0] == Players.BTC && gameBoard[1][0] == Players.BTC && gameBoard[2][0] == Players.BTC ) ||
                ( gameBoard[1][0] == Players.BTC && gameBoard[1][1] == Players.BTC && gameBoard[1][2] == Players.BTC ) ||
                ( gameBoard[2][0] == Players.BTC && gameBoard[1][1] == Players.BTC && gameBoard[0][2] == Players.BTC ) ||
                ( gameBoard[2][0] == Players.BTC && gameBoard[2][1] == Players.BTC && gameBoard[2][2] == Players.BTC ) ||
                ( gameBoard[0][1] == Players.BTC && gameBoard[1][1] == Players.BTC && gameBoard[2][1] == Players.BTC ) ||
                ( gameBoard[0][0] == Players.BTC && gameBoard[1][0] == Players.BTC && gameBoard[2][0] == Players.BTC ) ||
                ( gameBoard[0][2] == Players.BTC && gameBoard[1][2] == Players.BTC && gameBoard[2][2] == Players.BTC ) )
        {
            throw new Exception( "Player 2 (BTC) Wins!" );
        }
    }


}

