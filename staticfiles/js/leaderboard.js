function generate_leaderboard(members){

    const randomEmoji = () => {
    const emojis = ['👏', '👍', '🙌', '🤩', '🔥', '⭐️', '🏆', '💯'];
    let randomNumber = Math.floor(Math.random() * emojis.length);
    return emojis[randomNumber];
    };
    var rank=0
    members.forEach(member => {
    rank += 1
    if(member.username === current_player)
    {
        document.getElementById('current_player_rank').innerText = `${rank}/${members.length}`
        document.getElementById('current_player_score').innerText = member.score
    }
    let newRow = document.createElement('li');
    newRow.classList = 'c-list__item';
    newRow.innerHTML = `
            <div class="c-list__grid">
                <div class="c-flag c-place u-bg--transparent">${rank}</div>
                <div class="c-media">
                    <img class="c-avatar c-media__img" src="https://avatars.dicebear.com/api/identicon/${member.username}.svg?background=%23111111" alt=''/>
                    <div class="c-media__content">
                        <div class="c-media__title">${member.username}</div>
                        <a class="c-media__link u-text--small" href="https://127.0.0.1:8000/${member.handle}" target="_blank">@${member.school}</a>
                    </div>
                </div>
                <div class="u-text--right c-points">
                    <div class="u-mt--8">
                        <strong>${member.score}</strong> ${randomEmoji()}
                    </div>
                </div>
            </div>
        `;
    if (rank === 1) {
        newRow.querySelector('.c-place').classList.add('u-text--dark');
        newRow.querySelector('.c-place').classList.add('u-bg--yellow');
        newRow.querySelector('.c-points').classList.add('u-text--yellow');
    } else if (rank === 2) {
        newRow.querySelector('.c-place').classList.add('u-text--dark');
        newRow.querySelector('.c-place').classList.add('u-bg--teal');
        newRow.querySelector('.c-points').classList.add('u-text--teal');
    } else if (rank === 3) {
        newRow.querySelector('.c-place').classList.add('u-text--dark');
        newRow.querySelector('.c-place').classList.add('u-bg--orange');
        newRow.querySelector('.c-points').classList.add('u-text--orange');
    }
    list.appendChild(newRow); // ok i understood
    });

    // Find Winner by sorting points
    let winner = members[0];

    // Render winner card
    const winnerCard = document.getElementById('winner');
    winnerCard.innerHTML = `
        <div class="u-text-small u-text--medium u-mb--16">TOP PLAYER</div>
        <img class="c-avatar c-avatar--lg" src="https://avatars.dicebear.com/api/identicon/${winner.username}.svg?background=%23111111"/>
        <h3 class="u-mt--16">${winner.username}</h3>
        <span class="u-text--teal u-text--small">${winner.school}</span>
    `; 
}