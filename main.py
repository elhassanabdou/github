random = False
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.set_brightness(255)
strip.show_rainbow(1, 360)
music.set_tempo(250)

def on_every_interval():
    strip.rotate(1)
loops.every_interval(500, on_every_interval)

def on_forever():
    global random
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 20 and maqueen.ultrasonic(PingUnit.CENTIMETERS) != 0:
        random = Math.random_boolean()
        if random == True:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
            basic.pause(1000)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
            maqueen.motor_stop(maqueen.Motors.M1)
            basic.pause(800)
        if random == False:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
            basic.pause(1000)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.motor_stop(maqueen.Motors.M2)
            basic.pause(800)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
basic.forever(on_forever)

def on_forever2():
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play(music.tone_playable(196, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play(music.tone_playable(165, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.DOUBLE))
    music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play(music.tone_playable(233, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever2)

