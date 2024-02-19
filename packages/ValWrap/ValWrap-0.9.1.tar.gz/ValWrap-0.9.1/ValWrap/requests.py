from __future__ import annotations

from typing import List, TypedDict, Any
from typing_extensions import NotRequired

class All(TypedDict):
    AccountXP: AccountXPType
    ActivateContract: ActivateContractType
    ChangeQueue: ChangeQueueType
    ChangeQueueBody: ChangeQueueBodyType
    CompetitiveUpdates: CompetitiveUpdatesType
    Contracts: ContractsType
    CurrentGameLoadouts: CurrentGameLoadoutsType
    CurrentGameMatch: CurrentGameMatchType
    CurrentGamePlayer: CurrentGamePlayerType
    CustomGameConfigs: CustomGameConfigsType
    EnterMatchmakingQueue: EnterMatchmakingQueueType
    FetchContent: FetchContentType
    ItemUpgrades: ItemUpgradesType
    Leaderboard: LeaderboardType
    LeaveMatchmakingQueue: LeaveMatchmakingQueueType
    LockCharacter: LockCharacterType
    MatchDetails: MatchDetailsType
    MatchHistory: MatchHistoryType
    NameService: List[NameServiceType]
    NameServiceBody: List[str]
    OwnedItems: OwnedItemsType
    Party: PartyType
    PartyChatToken: PartyChatTokenType
    PartyDecline: PartyDeclineType
    PartyDisableCode: PartyDisableCodeType
    PartyGenerateCode: PartyGenerateCodeType
    PartyInvite: PartyInviteType
    PartyJoinByCode: PartyJoinByCodeType
    PartyPlayer: PartyPlayerType
    PartySetMemberReady: PartySetMemberReadyType
    PartySetMemberReadyBody: PartySetMemberReadyBodyType
    PartyVoiceToken: PartyVoiceTokenType
    Penalties: PenaltiesType
    PlayerLoadout: PlayerLoadoutType
    PlayerMMR: PlayerMMRType
    PreGameLoadouts: PreGameLoadoutsType
    PreGameMatch: PreGameMatchType
    PreGamePlayer: PreGamePlayerType
    Prices: PricesType
    RefreshCompetitiveTier: RefreshCompetitiveTierType
    RefreshPings: RefreshPingsType
    RefreshPlayerIdentity: RefreshPlayerIdentityType
    RiotGeo: RiotGeoType
    RiotGeoBody: RiotGeoBodyType
    SelectCharacter: SelectCharacterType
    SetCustomGameSettings: SetCustomGameSettingsType
    SetCustomGameSettingsBody: SetCustomGameSettingsBodyType
    SetPartyAccessibility: SetPartyAccessibilityType
    SetPartyAccessibilityBody: SetPartyAccessibilityBodyType
    SetPlayerLoadout: SetPlayerLoadoutType
    SetPlayerLoadoutBody: SetPlayerLoadoutBodyType
    StartCustomGame: StartCustomGameType
    Storefront: StorefrontType
    Wallet: WalletType

class AccountXPType(TypedDict):
    History: List[HistoryType]
    LastTimeGrantedFirstWin: str
    NextTimeFirstWinAvailable: str
    Progress: ProgressType
    Subject: str
    Version: float

class HistoryType(TypedDict):
    EndProgress: NotRequired[EndProgressType]
    ID: NotRequired[str]
    MatchStart: NotRequired[str]
    StartProgress: NotRequired[StartProgressType]
    XPDelta: NotRequired[float]
    XPMultipliers: NotRequired[List[Any]]
    XPSources: NotRequired[List[XpsourcesType]]
    GameStartTime: NotRequired[float]
    MatchID: NotRequired[str]
    QueueID: NotRequired[str]

class EndProgressType(TypedDict):
    Level: float
    XP: float

class StartProgressType(TypedDict):
    Level: float
    XP: float

class XpsourcesType(TypedDict):
    Amount: float
    ID: str

class ProgressType(TypedDict):
    Level: float
    XP: float

class ActivateContractType(TypedDict):
    ActiveSpecialContract: str
    Contracts: List[ContractsType]
    MissionMetadata: MissionMetadataType
    Missions: List[MissionsType]
    ProcessedMatches: List[ProcessedMatchesType]
    Subject: str
    Version: float

class MissionMetadataType(TypedDict):
    NPECompleted: bool
    WeeklyCheckpoint: str
    WeeklyRefillTime: str

class MissionsType(TypedDict):
    Complete: bool
    ExpirationTime: str
    ID: str
    Objectives: Any

class ProcessedMatchesType(TypedDict):
    ContractDeltas: Any
    CouldProgressMissions: bool
    ID: str
    MissionDeltas: Any
    RewardGrants: Any
    StartTime: float
    XPGrants: Any

class ChangeQueueType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class CheatDataType(TypedDict):
    ForcePostGameProcessing: bool
    GamePodOverride: str

class CustomGameDataType(TypedDict):
    AutobalanceEnabled: bool
    AutobalanceMinPlayers: float
    HasRecoveryData: bool
    MaxPartySize: float
    Membership: MembershipType
    Settings: SettingsType

class MembershipType(TypedDict):
    teamOne: Any
    teamOneCoaches: Any
    teamSpectate: Any
    teamTwo: Any
    teamTwoCoaches: Any

class SettingsType(TypedDict):
    GamePod: str
    GameRules: Any
    Map: str
    Mode: str
    UseBots: bool

class ErrorNotificationType(TypedDict):
    ErrorType: str
    ErroredPlayers: Any

class MatchmakingDataType(TypedDict):
    PreferredGamePods: List[str]
    QueueID: str
    SkillDisparityRRPenalty: float

class MembersType(TypedDict):
    CompetitiveTier: float
    IsModerator: bool
    IsOwner: bool
    IsReady: bool
    Pings: List[PingsType]
    PlatformType: str
    PlayerIdentity: PlayerIdentityType
    QueueEligibleRemainingAccountLevels: float
    SeasonalBadgeInfo: None
    Subject: str
    UseBroadcastHUD: bool

class PingsType(TypedDict):
    GamePodID: str
    Ping: float

class PlayerIdentityType(TypedDict):
    AccountLevel: float
    HideAccountLevel: bool
    Incognito: bool
    PlayerCardID: str
    PlayerTitleID: str
    PreferredLevelBorderID: Any
    Subject: str

class ChangeQueueBodyType(TypedDict):
    queueId: str

class CompetitiveUpdatesType(TypedDict):
    Matches: List[MatchesType]
    Subject: str
    Version: float

class MatchesType(TypedDict):
    AFKPenalty: float
    CompetitiveMovement: str
    MapID: str
    MatchID: str
    MatchStartTime: float
    RankedRatingAfterUpdate: float
    RankedRatingBeforeUpdate: float
    RankedRatingEarned: float
    RankedRatingPerformanceBonus: float
    SeasonID: str
    TierAfterUpdate: float
    TierBeforeUpdate: float

class ContractsType(TypedDict):
    ContractDefinitionID: NotRequired[str]
    ContractProgression: NotRequired[ContractProgressionType]
    ProgressionLevelReached: NotRequired[float]
    ProgressionTowardsNextLevel: NotRequired[float]
    ActiveSpecialContract: NotRequired[str]
    Contracts: NotRequired[List[ContractsType]]
    MissionMetadata: NotRequired[MissionMetadataType]
    Missions: NotRequired[List[MissionsType]]
    ProcessedMatches: NotRequired[List[ProcessedMatchesType]]
    Subject: NotRequired[str]
    Version: NotRequired[float]

class ContractProgressionType(TypedDict):
    HighestRewardedLevel: Any
    TotalProgressionEarned: float
    TotalProgressionEarnedVersion: float

class CurrentGameLoadoutsType(TypedDict):
    Loadouts: List[LoadoutsType]

class LoadoutsType(TypedDict):
    CharacterID: NotRequired[str]
    Loadout: NotRequired[LoadoutType]
    Expressions: NotRequired[ExpressionsType]
    Items: NotRequired[Any]
    Sprays: NotRequired[SpraysType]
    Subject: NotRequired[str]

class LoadoutType(TypedDict):
    Expressions: ExpressionsType
    Items: Any
    Sprays: SpraysType
    Subject: str

class ExpressionsType(TypedDict):
    AESSelections: List[AesselectionsType]

class AesselectionsType(TypedDict):
    AssetID: str
    SocketID: str
    TypeID: str

class SpraysType(TypedDict):
    SpraySelections: NotRequired[List[SpraySelectionsType]]
    EquipSlotID: NotRequired[str]
    SprayID: NotRequired[str]
    SprayLevelID: NotRequired[None]

class SpraySelectionsType(TypedDict):
    LevelID: str
    SocketID: str
    SprayID: str

class CurrentGameMatchType(TypedDict):
    AllMUCName: str
    ConnectionDetails: ConnectionDetailsType
    GamePodID: str
    IsReconnectable: bool
    MapID: str
    MatchID: str
    MatchmakingData: None
    ModeID: str
    Players: List[PlayersType]
    PostGameDetails: None
    ProvisioningFlow: str
    State: str
    TeamMUCName: str
    TeamMatchToken: str
    TeamVoiceID: str
    Version: float

class ConnectionDetailsType(TypedDict):
    GameClientHash: float
    GameServerHost: str
    GameServerHosts: List[str]
    GameServerObfuscatedIP: float
    GameServerPort: float
    PlayerKey: str

class PlayersType(TypedDict):
    IsAnonymized: NotRequired[bool]
    IsBanned: NotRequired[bool]
    PlayerCardID: NotRequired[str]
    TitleID: NotRequired[str]
    competitiveTier: NotRequired[float]
    gameName: NotRequired[str]
    leaderboardRank: NotRequired[float]
    numberOfWins: NotRequired[float]
    puuid: NotRequired[str]
    rankedRating: NotRequired[float]
    tagLine: NotRequired[str]
    CharacterID: NotRequired[str]
    CharacterSelectionState: NotRequired[str]
    CompetitiveTier: NotRequired[float]
    IsCaptain: NotRequired[bool]
    PlayerIdentity: NotRequired[PlayerIdentityType]
    PregamePlayerState: NotRequired[str]
    SeasonalBadgeInfo: NotRequired[SeasonalBadgeInfoType]
    Subject: NotRequired[str]
    accountLevel: NotRequired[float]
    behaviorFactors: NotRequired[BehaviorFactorsType]
    characterId: NotRequired[str]
    isObserver: NotRequired[bool]
    newPlayerExperienceDetails: NotRequired[NewPlayerExperienceDetailsType]
    partyId: NotRequired[str]
    platformInfo: NotRequired[PlatformInfoType]
    playerCard: NotRequired[str]
    playerTitle: NotRequired[str]
    preferredLevelBorder: NotRequired[Any]
    roundDamage: NotRequired[Any]
    sessionPlaytimeMinutes: NotRequired[Any]
    stats: NotRequired[Any]
    subject: NotRequired[str]
    teamId: NotRequired[Any]
    xpModifications: NotRequired[List[XpModificationsType]]
    IsAssociated: NotRequired[bool]
    IsCoach: NotRequired[bool]
    TeamID: NotRequired[Any]

class SeasonalBadgeInfoType(TypedDict):
    LeaderboardRank: float
    NumberOfWins: float
    Rank: float
    SeasonID: Any
    WinsByTier: None

class BehaviorFactorsType(TypedDict):
    afkRounds: float
    collisions: float
    commsRatingRecovery: float
    damageParticipationOutgoing: float
    friendlyFireIncoming: float
    friendlyFireOutgoing: float
    mouseMovement: float
    stayedInSpawnRounds: float

class NewPlayerExperienceDetailsType(TypedDict):
    ability: AbilityType
    adaptiveBots: AdaptiveBotsType
    basicGunSkill: BasicGunSkillType
    basicMovement: BasicMovementType
    bombPlant: BombPlantType
    defendBombSite: DefendBombSiteType
    settingStatus: SettingStatusType
    versionString: str

class AbilityType(TypedDict):
    idleTimeMillis: float
    objectiveCompleteTimeMillis: float

class AdaptiveBotsType(TypedDict):
    adaptiveBotAverageDurationMillisAllAttempts: float
    adaptiveBotAverageDurationMillisFirstAttempt: float
    idleTimeMillis: float
    killDetailsFirstAttempt: None
    objectiveCompleteTimeMillis: float

class BasicGunSkillType(TypedDict):
    idleTimeMillis: float
    objectiveCompleteTimeMillis: float

class BasicMovementType(TypedDict):
    idleTimeMillis: float
    objectiveCompleteTimeMillis: float

class BombPlantType(TypedDict):
    idleTimeMillis: float
    objectiveCompleteTimeMillis: float

class DefendBombSiteType(TypedDict):
    idleTimeMillis: float
    objectiveCompleteTimeMillis: float
    success: bool

class SettingStatusType(TypedDict):
    isCrosshairDefault: bool
    isMouseSensitivityDefault: bool

class PlatformInfoType(TypedDict):
    platformChipset: str
    platformOS: str
    platformOSVersion: str
    platformType: str

class XpModificationsType(TypedDict):
    ID: str
    Value: float

class CurrentGamePlayerType(TypedDict):
    MatchID: str
    Subject: str
    Version: float

class CustomGameConfigsType(TypedDict):
    Enabled: bool
    EnabledMaps: List[str]
    EnabledModes: List[str]
    GamePodPingServiceInfo: Any
    Queues: List[QueuesType]

class QueuesType(TypedDict):
    AllowFullPartyBypassSkillRestrictions: bool
    DisabledContent: List[Any]
    Enabled: bool
    FullPartyMaxCompetitiveTierRange: float
    GameRules: Any
    HighSkillTier: float
    InvalidPartySizes: List[float]
    IsRanked: bool
    IsTournament: bool
    MapWeights: List[str]
    MaxPartySize: float
    MaxPartySizeHighSkill: float
    MaxSkillTier: float
    MinPartySize: float
    MinimumAccountLevelRequired: float
    Mode: str
    NextScheduleChangeSeconds: float
    NumTeams: float
    PartyMaxCompetitiveTierRange: float
    PartyMaxCompetitiveTierRangePlacementBuffer: float
    PartySkillDisparityCompetitiveTiersCeilings: Any
    Priority: float
    QueueID: str
    RequireRoster: bool
    SupportedPlatformTypes: List[str]
    TeamSize: float
    TimeUntilNextScheduleChangeSeconds: float
    UseAccountLevelRequirement: bool
    queueFieldA: List[Any]

class EnterMatchmakingQueueType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class FetchContentType(TypedDict):
    DisabledIDs: List[Any]
    Events: List[EventsType]
    Seasons: List[SeasonsType]

class EventsType(TypedDict):
    EndTime: str
    ID: str
    IsActive: bool
    Name: str
    StartTime: str

class SeasonsType(TypedDict):
    EndTime: str
    ID: str
    IsActive: bool
    Name: str
    StartTime: str
    Type: str

class ItemUpgradesType(TypedDict):
    Definitions: List[DefinitionsType]

class DefinitionsType(TypedDict):
    ID: str
    Item: ItemType
    ProgressionSchedule: ProgressionScheduleType
    RequiredEntitlement: RequiredEntitlementType
    RewardSchedule: RewardScheduleType
    Sidegrades: Any

class ItemType(TypedDict):
    ItemID: str
    ItemTypeID: str
    Amount: NotRequired[float]

class ProgressionScheduleType(TypedDict):
    Name: str
    ProgressionCurrencyID: str
    ProgressionDeltaPerLevel: Any

class RequiredEntitlementType(TypedDict):
    ItemID: str
    ItemTypeID: str

class RewardScheduleType(TypedDict):
    ID: str
    Name: str
    Prerequisites: None
    RewardsPerLevel: Any

class LeaderboardType(TypedDict):
    Deployment: str
    Players: List[PlayersType]
    QueueID: str
    SeasonID: str
    immortalStartingIndex: float
    immortalStartingPage: float
    query: str
    startIndex: float
    tierDetails: Any
    topTierRRThreshold: float
    totalPlayers: float

class LeaveMatchmakingQueueType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class LockCharacterType(TypedDict):
    AllyTeam: Any
    BannedMapIDs: List[Any]
    CastedVotes: Any
    EnemyTeam: Any
    EnemyTeamLockCount: float
    EnemyTeamSize: float
    GamePodID: str
    ID: str
    IsRanked: bool
    LastUpdated: str
    MUCName: str
    MapID: str
    MapSelectPool: List[Any]
    MapSelectStep: float
    MapSelectSteps: List[Any]
    MatchCoaches: List[Any]
    Mode: str
    ObserverSubjects: List[Any]
    PhaseTimeRemainingNS: float
    PregameState: str
    ProvisioningFlowID: str
    QueueID: Any
    RosterMetadata: None
    StepTimeRemainingNS: float
    Team1: Any
    TeamMatchToken: str
    Teams: List[TeamsType]
    TournamentMetadata: None
    Version: float
    VoiceSessionID: str
    altModesFlagADA: bool

class TeamsType(TypedDict):
    Players: List[PlayersType]
    TeamID: Any

class MatchDetailsType(TypedDict):
    bots: List[Any]
    coaches: List[CoachesType]
    kills: Any
    matchInfo: MatchInfoType
    players: List[PlayersType]
    roundResults: Any
    teams: Any

class CoachesType(TypedDict):
    subject: str
    teamId: str

class MatchInfoType(TypedDict):
    completionState: str
    customGameName: str
    forcePostProcessing: bool
    gameLengthMillis: Any
    gameLoopZone: str
    gameMode: str
    gamePodId: str
    gameServerAddress: str
    gameStartMillis: float
    gameVersion: str
    isCompleted: bool
    isMatchSampled: bool
    isRanked: bool
    mapId: str
    matchId: str
    partyRRPenalties: Any
    platformType: str
    premierMatchInfo: Any
    provisioningFlowID: str
    queueID: str
    seasonId: str
    shouldMatchDisablePenalties: bool

class MatchHistoryType(TypedDict):
    BeginIndex: float
    EndIndex: float
    History: List[HistoryType]
    Subject: str
    Total: float

class NameServiceType(TypedDict):
    DisplayName: str
    GameName: str
    Subject: str
    TagLine: str

class OwnedItemsType(TypedDict):
    EntitlementsByTypes: List[EntitlementsByTypesType]

class EntitlementsByTypesType(TypedDict):
    Entitlements: List[EntitlementsType]
    ItemTypeID: str

class EntitlementsType(TypedDict):
    InstanceID: str
    ItemID: str
    TypeID: str

class PartyType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class PartyChatTokenType(TypedDict):
    Room: str
    Token: str

class PartyDeclineType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class PartyDisableCodeType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class PartyGenerateCodeType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class PartyInviteType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class PartyJoinByCodeType(TypedDict):
    CurrentPartyID: str
    Invites: None
    PlatformInfo: PlatformInfoType
    Requests: List[RequestsType]
    Subject: str
    Version: float

class RequestsType(TypedDict):
    CreatedAt: str
    ExpiresIn: float
    ID: str
    PartyID: str
    RefreshedAt: str
    RequestedBySubject: str
    Subjects: List[str]

class PartyPlayerType(TypedDict):
    CurrentPartyID: str
    Invites: None
    PlatformInfo: PlatformInfoType
    Requests: List[RequestsType]
    Subject: str
    Version: float

class PartySetMemberReadyType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class PartySetMemberReadyBodyType(TypedDict):
    ready: bool

class PartyVoiceTokenType(TypedDict):
    Room: str
    Token: str

class PenaltiesType(TypedDict):
    Penalties: List[Any]
    Subject: str
    Version: float

class PlayerLoadoutType(TypedDict):
    Guns: List[GunsType]
    Identity: IdentityType
    Incognito: bool
    Sprays: List[SpraysType]
    Subject: str
    Version: float

class GunsType(TypedDict):
    Attachments: List[Any]
    CharmID: str
    CharmInstanceID: str
    CharmLevelID: str
    ChromaID: str
    ID: str
    SkinID: str
    SkinLevelID: str

class IdentityType(TypedDict):
    AccountLevel: float
    HideAccountLevel: bool
    PlayerCardID: str
    PlayerTitleID: str
    PreferredLevelBorderID: str

class PlayerMMRType(TypedDict):
    IsActRankBadgeHidden: bool
    IsLeaderboardAnonymized: bool
    LatestCompetitiveUpdate: LatestCompetitiveUpdateType
    NewPlayerExperienceFinished: bool
    QueueSkills: Any
    Subject: str
    Version: float

class LatestCompetitiveUpdateType(TypedDict):
    AFKPenalty: float
    CompetitiveMovement: str
    MapID: str
    MatchID: str
    MatchStartTime: float
    RankedRatingAfterUpdate: float
    RankedRatingBeforeUpdate: float
    RankedRatingEarned: float
    RankedRatingPerformanceBonus: float
    SeasonID: str
    TierAfterUpdate: float
    TierBeforeUpdate: float

class PreGameLoadoutsType(TypedDict):
    Loadouts: List[LoadoutsType]
    LoadoutsValid: bool

class PreGameMatchType(TypedDict):
    AllyTeam: Any
    BannedMapIDs: List[Any]
    CastedVotes: Any
    EnemyTeam: Any
    EnemyTeamLockCount: float
    EnemyTeamSize: float
    GamePodID: str
    ID: str
    IsRanked: bool
    LastUpdated: str
    MUCName: str
    MapID: str
    MapSelectPool: List[Any]
    MapSelectStep: float
    MapSelectSteps: List[Any]
    MatchCoaches: List[Any]
    Mode: str
    ObserverSubjects: List[Any]
    PhaseTimeRemainingNS: float
    PregameState: str
    ProvisioningFlowID: str
    QueueID: Any
    RosterMetadata: None
    StepTimeRemainingNS: float
    Team1: Any
    TeamMatchToken: str
    Teams: List[TeamsType]
    TournamentMetadata: None
    Version: float
    VoiceSessionID: str
    altModesFlagADA: bool

class PreGamePlayerType(TypedDict):
    MatchID: str
    Subject: str
    Version: float

class PricesType(TypedDict):
    Offers: List[OffersType]

class OffersType(TypedDict):
    Cost: Any
    IsDirectPurchase: bool
    OfferID: str
    Rewards: List[RewardsType]
    StartDate: str

class RewardsType(TypedDict):
    ItemID: str
    ItemTypeID: str
    Quantity: float

class RefreshCompetitiveTierType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class RefreshPingsType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class RefreshPlayerIdentityType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class RiotGeoType(TypedDict):
    affinities: AffinitiesType
    token: str

class AffinitiesType(TypedDict):
    live: str
    pbe: str

class RiotGeoBodyType(TypedDict):
    id_token: str

class SelectCharacterType(TypedDict):
    AllyTeam: Any
    BannedMapIDs: List[Any]
    CastedVotes: Any
    EnemyTeam: Any
    EnemyTeamLockCount: float
    EnemyTeamSize: float
    GamePodID: str
    ID: str
    IsRanked: bool
    LastUpdated: str
    MUCName: str
    MapID: str
    MapSelectPool: List[Any]
    MapSelectStep: float
    MapSelectSteps: List[Any]
    MatchCoaches: List[Any]
    Mode: str
    ObserverSubjects: List[Any]
    PhaseTimeRemainingNS: float
    PregameState: str
    ProvisioningFlowID: str
    QueueID: Any
    RosterMetadata: None
    StepTimeRemainingNS: float
    Team1: Any
    TeamMatchToken: str
    Teams: List[TeamsType]
    TournamentMetadata: None
    Version: float
    VoiceSessionID: str
    altModesFlagADA: bool

class SetCustomGameSettingsType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class SetCustomGameSettingsBodyType(TypedDict):
    GamePod: str
    GameRules: GameRulesType
    Map: str
    Mode: str
    UseBots: bool

class GameRulesType(TypedDict):
    AllowGameModifiers: str
    IsOvertimeWinByTwo: str
    PlayOutAllRounds: str
    SkipMatchHistory: str
    TournamentMode: str

class SetPartyAccessibilityType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class SetPartyAccessibilityBodyType(TypedDict):
    accessibility: str

class SetPlayerLoadoutType(TypedDict):
    Guns: List[GunsType]
    Identity: IdentityType
    Incognito: bool
    Sprays: List[SpraysType]
    Subject: str
    Version: float

class SetPlayerLoadoutBodyType(TypedDict):
    Guns: List[GunsType]
    Identity: IdentityType
    Incognito: bool
    Sprays: List[SpraysType]

class StartCustomGameType(TypedDict):
    Accessibility: str
    CheatData: CheatDataType
    ClientVersion: str
    CustomGameData: CustomGameDataType
    EligibleQueues: List[str]
    ErrorNotification: ErrorNotificationType
    ID: str
    InviteCode: str
    Invites: None
    MUCName: str
    MatchmakingData: MatchmakingDataType
    Members: List[MembersType]
    PreviousState: str
    QueueEntryTime: str
    QueueIneligibilities: List[str]
    Requests: List[Any]
    RestrictedSeconds: float
    State: str
    StateTransitionReason: str
    Version: float
    VoiceRoomID: str
    XPBonuses: List[Any]

class StorefrontType(TypedDict):
    AccessoryStore: AccessoryStoreType
    BonusStore: BonusStoreType
    FeaturedBundle: FeaturedBundleType
    SkinsPanelLayout: SkinsPanelLayoutType
    UpgradeCurrencyStore: UpgradeCurrencyStoreType

class AccessoryStoreType(TypedDict):
    AccessoryStoreOffers: List[AccessoryStoreOffersType]
    AccessoryStoreRemainingDurationInSeconds: float
    StorefrontID: str

class AccessoryStoreOffersType(TypedDict):
    ContractID: str
    Offer: OfferType

class OfferType(TypedDict):
    Cost: Any
    IsDirectPurchase: bool
    OfferID: str
    Rewards: List[RewardsType]
    StartDate: str

class BonusStoreType(TypedDict):
    BonusStoreOffers: List[BonusStoreOffersType]
    BonusStoreRemainingDurationInSeconds: float

class BonusStoreOffersType(TypedDict):
    BonusOfferID: str
    DiscountCosts: Any
    DiscountPercent: float
    IsSeen: bool
    Offer: OfferType

class FeaturedBundleType(TypedDict):
    Bundle: BundleType
    BundleRemainingDurationInSeconds: float
    Bundles: List[BundlesType]

class BundleType(TypedDict):
    CurrencyID: str
    DataAssetID: str
    DurationRemainingInSeconds: float
    ID: str
    ItemOffers: Any
    Items: List[ItemsType]
    TotalBaseCost: Any
    TotalDiscountPercent: float
    TotalDiscountedCost: Any
    WholesaleOnly: bool

class ItemsType(TypedDict):
    BasePrice: float
    CurrencyID: str
    DiscountPercent: float
    DiscountedPrice: float
    IsPromoItem: bool
    Item: ItemType

class BundlesType(TypedDict):
    CurrencyID: str
    DataAssetID: str
    DurationRemainingInSeconds: float
    ID: str
    ItemOffers: Any
    Items: List[ItemsType]
    TotalBaseCost: Any
    TotalDiscountPercent: float
    TotalDiscountedCost: Any
    WholesaleOnly: bool

class SkinsPanelLayoutType(TypedDict):
    SingleItemOffers: List[str]
    SingleItemOffersRemainingDurationInSeconds: float
    SingleItemStoreOffers: List[SingleItemStoreOffersType]

class SingleItemStoreOffersType(TypedDict):
    Cost: Any
    IsDirectPurchase: bool
    OfferID: str
    Rewards: List[RewardsType]
    StartDate: str

class UpgradeCurrencyStoreType(TypedDict):
    UpgradeCurrencyOffers: List[UpgradeCurrencyOffersType]

class UpgradeCurrencyOffersType(TypedDict):
    DiscountedPercent: float
    Offer: OfferType
    OfferID: str
    StorefrontItemID: str

class WalletType(TypedDict):
    Balances: Any


NameServiceBodyType = List[str]


from typing import Optional
from ValLib import Auth, ExtraAuth, get, post, put, delete


def get_fetch_content(auth: ExtraAuth) -> FetchContentType:
	api_url = f"https://shared.{auth.shard}.a.pvp.net/content-service/v3/content"
	res = get(api_url, auth)
	return res

def get_account_xp(auth: ExtraAuth, puuid: Optional[str] = None) -> AccountXPType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/account-xp/v1/players/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_player_loadout(auth: ExtraAuth, puuid: Optional[str] = None) -> PlayerLoadoutType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/personalization/v2/players/{puuid or auth.user_id}/playerloadout"
	res = get(api_url, auth)
	return res

def put_set_player_loadout(auth: ExtraAuth, data: SetPlayerLoadoutBodyType, puuid: Optional[str] = None) -> SetPlayerLoadoutType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/personalization/v2/players/{puuid or auth.user_id}/playerloadout"
	res = put(api_url, auth, data)
	return res

def get_player_mmr(auth: ExtraAuth, puuid: Optional[str] = None) -> PlayerMMRType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/mmr/v1/players/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_match_history(auth: ExtraAuth, puuid: Optional[str] = None) -> MatchHistoryType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/match-history/v1/history/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_match_details(auth: ExtraAuth, matchID: str) -> MatchDetailsType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/match-details/v1/matches/{matchID}"
	res = get(api_url, auth)
	return res

def get_competitive_updates(auth: ExtraAuth, puuid: Optional[str] = None) -> CompetitiveUpdatesType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/mmr/v1/players/{puuid or auth.user_id}/competitiveupdates"
	res = get(api_url, auth)
	return res

def get_leaderboard(auth: ExtraAuth, season_id: str) -> LeaderboardType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/mmr/v1/leaderboards/affinity/na/queue/competitive/season/{season_id}"
	res = get(api_url, auth)
	return res

def get_penalties(auth: ExtraAuth) -> PenaltiesType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/restrictions/v3/penalties"
	res = get(api_url, auth)
	return res

def put_name_service(auth: ExtraAuth, data: NameServiceBodyType) -> List[NameServiceType]:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/name-service/v2/players"
	res = put(api_url, auth, data)
	return res

def get_party(auth: ExtraAuth, party_id: str) -> PartyType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}"
	res = get(api_url, auth)
	return res

def get_party_player(auth: ExtraAuth, puuid: Optional[str] = None) -> PartyPlayerType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/players/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def delete_party_remove_player(auth: ExtraAuth, puuid: Optional[str] = None) -> Any:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/players/{puuid or auth.user_id}"
	res = delete(api_url, auth)
	return res

def post_party_set_member_ready(auth: ExtraAuth, data: PartySetMemberReadyBodyType, party_id: str, puuid: Optional[str] = None) -> PartySetMemberReadyType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/members/{puuid or auth.user_id}/setReady"
	res = post(api_url, auth, data)
	return res

def post_refresh_competitive_tier(auth: ExtraAuth, party_id: str, puuid: Optional[str] = None) -> RefreshCompetitiveTierType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/members/{puuid or auth.user_id}/refreshCompetitiveTier"
	res = post(api_url, auth)
	return res

def post_refresh_player_identity(auth: ExtraAuth, party_id: str, puuid: Optional[str] = None) -> RefreshPlayerIdentityType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/members/{puuid or auth.user_id}/refreshPlayerIdentity"
	res = post(api_url, auth)
	return res

def post_refresh_pings(auth: ExtraAuth, party_id: str, puuid: Optional[str] = None) -> RefreshPingsType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/members/{puuid or auth.user_id}/refreshPings"
	res = post(api_url, auth)
	return res

def post_change_queue(auth: ExtraAuth, data: ChangeQueueBodyType, party_id: str) -> ChangeQueueType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/queue"
	res = post(api_url, auth, data)
	return res

def post_start_custom_game(auth: ExtraAuth, party_id: str) -> StartCustomGameType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/startcustomgame"
	res = post(api_url, auth)
	return res

def post_enter_matchmaking_queue(auth: ExtraAuth, party_id: str) -> EnterMatchmakingQueueType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/matchmaking/join"
	res = post(api_url, auth)
	return res

def post_leave_matchmaking_queue(auth: ExtraAuth, party_id: str) -> LeaveMatchmakingQueueType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/matchmaking/leave"
	res = post(api_url, auth)
	return res

def post_set_party_accessibility(auth: ExtraAuth, data: SetPartyAccessibilityBodyType, party_id: str) -> SetPartyAccessibilityType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/accessibility"
	res = post(api_url, auth, data)
	return res

def post_set_custom_game_settings(auth: ExtraAuth, data: SetCustomGameSettingsBodyType, party_id: str) -> SetCustomGameSettingsType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/customgamesettings"
	res = post(api_url, auth, data)
	return res

def post_party_invite(auth: ExtraAuth, party_id: str, name: str, tagline: str) -> PartyInviteType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/invites/name/{name}/tag/{tagline}"
	res = post(api_url, auth)
	return res

def post_party_request(auth: ExtraAuth, party_id: str) -> Any:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/request"
	res = post(api_url, auth)
	return res

def post_party_decline(auth: ExtraAuth, party_id: str, request_id: str) -> PartyDeclineType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/request/{request_id}/decline"
	res = post(api_url, auth)
	return res

def get_custom_game_configs(auth: ExtraAuth) -> CustomGameConfigsType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/customgameconfigs"
	res = get(api_url, auth)
	return res

def get_party_chat_token(auth: ExtraAuth, party_id: str) -> PartyChatTokenType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net//parties/v1/parties/{party_id}/muctoken"
	res = get(api_url, auth)
	return res

def get_party_voice_token(auth: ExtraAuth, party_id: str) -> PartyVoiceTokenType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net//parties/v1/parties/{party_id}/voicetoken"
	res = get(api_url, auth)
	return res

def delete_party_disable_code(auth: ExtraAuth, party_id: str) -> PartyDisableCodeType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/invitecode"
	res = delete(api_url, auth)
	return res

def post_party_generate_code(auth: ExtraAuth, party_id: str) -> PartyGenerateCodeType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/parties/{party_id}/invitecode"
	res = post(api_url, auth)
	return res

def post_party_join_by_code(auth: ExtraAuth, code: str) -> PartyJoinByCodeType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/parties/v1/players/joinbycode/{code}"
	res = post(api_url, auth)
	return res

def get_prices(auth: ExtraAuth) -> PricesType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/store/v1/offers"
	res = get(api_url, auth)
	return res

def get_storefront(auth: ExtraAuth, puuid: Optional[str] = None) -> StorefrontType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/store/v2/storefront/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_wallet(auth: ExtraAuth, puuid: Optional[str] = None) -> WalletType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/store/v1/wallet/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_owned_items(auth: ExtraAuth, ItemTypeID: str, puuid: Optional[str] = None) -> OwnedItemsType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/store/v1/entitlements/{puuid or auth.user_id}/{ItemTypeID}"
	res = get(api_url, auth)
	return res

def get_pregame_player(auth: ExtraAuth, puuid: Optional[str] = None) -> PreGamePlayerType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/pregame/v1/players/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_pregame_match(auth: ExtraAuth, match_id: str) -> PreGameMatchType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/pregame/v1/matches/{match_id}"
	res = get(api_url, auth)
	return res

def get_pregame_loadouts(auth: ExtraAuth, match_id: str) -> PreGameLoadoutsType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/pregame/v1/matches/{match_id}/loadouts"
	res = get(api_url, auth)
	return res

def post_select_character(auth: ExtraAuth, match_id: str, agent_id: str) -> SelectCharacterType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/pregame/v1/matches/{match_id}/select/{agent_id}"
	res = post(api_url, auth)
	return res

def post_lock_character(auth: ExtraAuth, match_id: str, agent_id: str) -> LockCharacterType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/pregame/v1/matches/{match_id}/lock/{agent_id}"
	res = post(api_url, auth)
	return res

def post_pregame_quit(auth: ExtraAuth, match_id: str) -> Any:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/pregame/v1/matches/{match_id}/quit"
	res = post(api_url, auth)
	return res

def get_current_game_player(auth: ExtraAuth, puuid: Optional[str] = None) -> CurrentGamePlayerType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/core-game/v1/players/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def get_current_game_match(auth: ExtraAuth, match_id: str) -> CurrentGameMatchType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/core-game/v1/matches/{match_id}"
	res = get(api_url, auth)
	return res

def get_current_game_loadouts(auth: ExtraAuth, match_id: str) -> CurrentGameLoadoutsType:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/core-game/v1/matches/{match_id}/loadouts"
	res = get(api_url, auth)
	return res

def post_current_game_quit(auth: ExtraAuth, match_id: str, puuid: Optional[str] = None) -> Any:
	api_url = f"https://glz-{auth.region}-1.{auth.shard}.a.pvp.net/core-game/v1/players/{puuid or auth.user_id}/disassociate/{match_id}"
	res = post(api_url, auth)
	return res

def get_item_upgrades(auth: ExtraAuth) -> ItemUpgradesType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/contract-definitions/v3/item-upgrades"
	res = get(api_url, auth)
	return res

def get_contracts(auth: ExtraAuth, puuid: Optional[str] = None) -> ContractsType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/contracts/v1/contracts/{puuid or auth.user_id}"
	res = get(api_url, auth)
	return res

def post_activate_contract(auth: ExtraAuth, contract_id: str, puuid: Optional[str] = None) -> ActivateContractType:
	api_url = f"https://pd.{auth.shard}.a.pvp.net/contracts/v1/contracts/{puuid or auth.user_id}/special/{contract_id}"
	res = post(api_url, auth)
	return res

def put_riot_geo(auth: Auth, data: RiotGeoBodyType) -> RiotGeoType:
	api_url = "https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant"
	res = put(api_url, auth, data)
	return res

def get_pas_token(auth: Auth) -> PASTokenType:
	api_url = "https://riot-geo.pas.si.riotgames.com/pas/v1/service/chat"
	res = get(api_url, auth)
	return res

def get_riot_client_config(auth: Auth) -> Any:
	api_url = "https://clientconfig.rpg.riotgames.com/api/v1/config/player?app=Riot%20Client"
	res = get(api_url, auth)
	return res

__all__ = ["get_fetch_content","get_account_xp","get_player_loadout","put_set_player_loadout","get_player_mmr","get_match_history","get_match_details","get_competitive_updates","get_leaderboard","get_penalties","put_name_service","get_party","get_party_player","delete_party_remove_player","post_party_set_member_ready","post_refresh_competitive_tier","post_refresh_player_identity","post_refresh_pings","post_change_queue","post_start_custom_game","post_enter_matchmaking_queue","post_leave_matchmaking_queue","post_set_party_accessibility","post_set_custom_game_settings","post_party_invite","post_party_request","post_party_decline","get_custom_game_configs","get_party_chat_token","get_party_voice_token","delete_party_disable_code","post_party_generate_code","post_party_join_by_code","get_prices","get_storefront","get_wallet","get_owned_items","get_pregame_player","get_pregame_match","get_pregame_loadouts","post_select_character","post_lock_character","post_pregame_quit","get_current_game_player","get_current_game_match","get_current_game_loadouts","post_current_game_quit","get_item_upgrades","get_contracts","post_activate_contract","put_riot_geo","get_pas_token","get_riot_client_config"]
