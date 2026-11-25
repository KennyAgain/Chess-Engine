import pygame
import Engine
pygame.init()

W,H = 720,720
Field_Size = W/8
screen = pygame.display.set_mode((W,H))

Piece_Sprite_Sheet_Path = "Pieces.png"
Piece_Size = Field_Size

Piece_Sprite_Sheet = pygame.image.load(Piece_Sprite_Sheet_Path)
Piece_Sprite_Sheet = pygame.transform.scale(Piece_Sprite_Sheet,(Field_Size*6,Field_Size*2))#after loading the piece sheet resize to fit for board
print(Piece_Sprite_Sheet.get_size())
Green_1 = 	(238,238,210)
Green_2 = 	(118,150,86)

clock = pygame.time.Clock()

picked_up_piece = -1 #the index of the current picked up piece in the board.piceces array

def draw_board(board):
    for F_X in range(8):
        for F_Y in range(8):
            field_color = Green_1 if (F_X + F_Y) % 2 == 0 else Green_2
            x,y = F_X * Field_Size, F_Y * Field_Size
            pygame.draw.rect(screen,field_color,(x,y,x+Field_Size,y+Field_Size))

            if board.board[F_X][F_Y] == 0:
                continue

            type = board.pieces[board.board[F_X][F_Y]-1].type 
            color = board.pieces[board.board[F_X][F_Y]-1].color

            offset_x,offset_y = (type-1)*Field_Size,color*Field_Size #use the type as an index for offset in the sheet
            Piece_Image = Piece_Sprite_Sheet.subsurface((offset_x,offset_y,Field_Size,Field_Size))

            screen.blit(Piece_Image,(x,y))

def handle_piece_move(x,y,board):
    global picked_up_piece
    index_x, index_y = int(x//Field_Size),int(y//Field_Size)
    if picked_up_piece < 0: #there currently isnt a picked up piece
        picked_up_piece = board.board[index_x][index_y]
    else:
        board.move(picked_up_piece,index_x,index_y) #attempts to move the piece 
        if board.succes: #only if Engine returns succeses the piece is put down
            print(picked_up_piece)
            board.succes = False
            picked_up_piece = -1
        

def main():
    board = Engine.Board()
    mouse_clicked = False
    last_mouse_state = False

    while True:
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = pygame.mouse.get_pressed()[0]
                mouse_pos = pygame.mouse.get_pos()

        draw_board(board)

        if not mouse_clicked == last_mouse_state:
            last_mouse_state = mouse_clicked
            handle_piece_move(mouse_pos[0],mouse_pos[1],board)

        pygame.display.flip() 
        clock.tick(60)        


if __name__ == "__main__":
    main()