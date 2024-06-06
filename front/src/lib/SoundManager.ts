let sounds: Sound[] = [];

export type Sound = {
    src: string,
    volume: number,
    id: string,
    audioObject?: HTMLAudioElement
}

export function playSound(src: string, volume: number = 1, loop: boolean = false): string {
    let id = Math.random().toString(36).substring(7);
    let audio = new Audio(src);
    audio.volume = volume;
    audio.loop = loop;
    audio.play();

    sounds.push({
        src,
        volume,
        id,
        audioObject: audio
    })

    return id;
}

export function stopSound(id: string) {
    let index = sounds.findIndex(sound => sound.id == id);
    if (index == -1) { return }

    sounds[index].audioObject?.pause();
    sounds.splice(index, 1);
}