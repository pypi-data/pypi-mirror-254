from dash import Dash, html
from dash_canvas import DashCanvas
from dash_canvas.utils.io_utils import array_to_data_url
import numpy as np

def get_canvas(canvas_height=500, canvas_width=1000, line_width=5, line_color='white', color=31):
    '''
    Create emty canvas.

    :param canvas_height int Height of canvas
    :param canvas_width int Width of canvas
    :param line_width int Width of draw line
    :param line_color str Color of draw line
    :param color int Color of background [r, g, b] * color
    
    '''

    background_width = 10
    background_height = 10
    background_image = np.ones((background_width, background_height, 3), dtype=np.uint8) * color
    background = array_to_data_url(background_image)

    app = Dash(__name__)

    app.layout = html.Div(
                DashCanvas(
                    width=canvas_width,
                    height=canvas_height,
                    lineWidth=line_width,
                    image_content=background,
                    hide_buttons=['line', 'zoom', 'rectangle', 'select'],
                    lineColor=line_color))
    
    app.run(debug=True)

