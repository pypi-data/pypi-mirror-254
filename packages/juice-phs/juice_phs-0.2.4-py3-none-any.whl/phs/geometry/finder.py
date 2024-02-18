import spiceypy as spice
import logging
from phs.utils.time import win2lst, sec2hhmmss

def target_in_fov(utc_start='', utc_end='',
                  interval=False, step=600,
                  fov='JUICE_JANUS',
                  observer=None, # Required when the FOV is not an ephemeris object.
                  target='SUN',
                  occtyp='ANY',
                  verbose=False,
                  abcorr='NONE',
                  **kwargs):
    """
    Check the visibility of a target in a Field of View (FOV) over a specified time interval.

    Parameters
    ----------
    utc_start : str, optional
        Start time in UTC format (default is '').
    utc_end : str, optional
        End time in UTC format (default is '').
    interval : SPICE window, optional
        Time interval specified as a SPICE window (default is False).
    step : int, optional
        Step size for time increments (default is 600).
    fov : str, optional
        Name of the Field of View (FOV) (default is 'JUICE_JANUS').
    observer : str, optional
        Name of the observer object (required when FOV is not an ephemeris object).
    target : str, optional
        Target object to check visibility (default is 'SUN').
    occtyp : str, optional
        Type of occultation (default is 'ANY').
    verbose : bool, optional
        Toggle verbose logging (default is False).
    abcorr : str, optional
        Aberration correction (default is 'NONE').
    **kwargs : dict, optional
        Additional keyword arguments.

    Returns
    -------
    riswin : spice.cell_double
        SPICE window containing time intervals when the target is visible in the FOV.
    rislis : list
        List of start and stop times within the detected intervals.

    Notes
    -----
    This function determines the visibility of a target in a specified Field of View (FOV) over a given time interval. It calculates the intervals during which the target is visible from the observer within the specified FOV.

    When 'interval' is False, 'utc_start' and 'utc_end' define the time interval to be analyzed. If 'interval' is provided, it overrides 'utc_start' and 'utc_end'.

    If 'observer' is not provided, it defaults to the FOV name.
    """
    if not interval:
        et_start = spice.utc2et(utc_start)
        et_stop = spice.utc2et(utc_end)
        cnfine = spice.cell_double(2)
        spice.wninsd(et_start, et_stop, cnfine)
    else:
        cnflst = win2lst(interval, verbose=False)
        utc_start = spice.et2utc(min(cnflst)[0], 'ISOC', 0, 70)
        utc_end = spice.et2utc(max(cnflst)[-1], 'ISOC', 0, 70)
        cnfine = interval

    riswin = spice.cell_double(40000)

    if not observer:
        observer = fov

    spice.gftfov(fov, target, 'ELLIPSOID', f'IAU_{target}',
                 abcorr, observer, step, cnfine, riswin)

    # The function wncard returns the number of intervals
    # in a SPICE window.
    winsiz = spice.wncard(riswin)

    # Define the list of events.
    rislis = []

    if winsiz == 0 and verbose:
        logging.warning(f'{target} not in {fov} FOV')
    else:
        # Display the visibility time periods.
        if verbose:
            logging.info('')
            logging.info(f'{target} in {fov} FOV')
            logging.info('------------------------------------------------------')
            logging.info(f'Interval start:     {utc_start}')
            logging.info(f'Interval end:       {utc_end}')
            logging.info(f'Step [s]:           {step}')
            logging.info('-----------------------------------------------------')

        for i in range(winsiz):
            # Fetch the start and stop times of
            # the ith interval from the search result
            # window riswin.
            [intbeg, intend] = spice.wnfetd(riswin, i)

            # Convert the time to a UTC calendar string.
            timstr_beg = spice.et2utc(intbeg, 'ISOC', 0, 70)
            timstr_end = spice.et2utc(intend, 'ISOC', 0, 70)
            duration = intend - intbeg

            # Write the string to standard output.
            if verbose:
                logging.info(f'{timstr_beg} - {timstr_end}: {sec2hhmmss(duration)}')

            rislis.append([intbeg, intend])
        if verbose:
            logging.info('-----------------------------------------------------')
            logging.info(f'Number of results: {len(rislis)}')
            logging.info('')

    return riswin, rislis