def ipywidgets_update(func, data, options={}, **kwargs):
    ''' A general ipywidgets update function that can be passed to ipywidgets.interactive. To use this, you can run:

    import ipywidgets as widgets
    import plotter.interactive as plint

    w = widgets.interactive(plint.ipywidgets_update, func=widgets.fixed(my_func), plot_data=widgets.fixed(plot_data), options=widgets.fixed(options), key1=widget1, key2=widget2, key3=widget3)

    where key1, key2, key3 etc. are the values in the options-dictionary you want widget control of, and widget1, widget2, widget3 etc. are widgets to control these values, e.g. widgets.IntSlider(value=1, min=0, max=10)
    '''

    # Update the options-dictionary with the values from the widgets
    for key in kwargs:
        options[key] = kwargs[key]

    # Call the function with the plot_data and options-dictionaries
    func(data=data, options=options)