-- FiveM Client Script Example
local ESX = nil

Citizen.CreateThread(function()
    while ESX == nil do
        TriggerEvent('esx:getSharedObject', function(obj) ESX = obj end)
        Citizen.Wait(0)
    end
end)

RegisterNetEvent('test:clientEvent')
AddEventHandler('test:clientEvent', function(data)
    print('Received data:', data)
end)

function TestFunction()
    local playerPed = PlayerPedId()
    local playerCoords = GetEntityCoords(playerPed)
    
    print('Player coordinates:', playerCoords)
    
    return {
        x = playerCoords.x,
        y = playerCoords.y,
        z = playerCoords.z
    }
end

-- Main execution
Citizen.CreateThread(function()
    while true do
        Citizen.Wait(5000)
        TestFunction()
    end
end)