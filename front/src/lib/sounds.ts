export function playSound(sound: string, volume: number = 1) {
    console.info(`Playing sound: ${sound}`)

    let audio = new Audio(`/${sound}`);
    audio.volume = volume;
    audio.play();
}